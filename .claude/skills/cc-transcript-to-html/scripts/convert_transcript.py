#!/usr/bin/env python3
"""Convert Claude Code JSONL transcript to readable HTML.

Usage:
    python convert_transcript.py <input.jsonl> [output.html]

If output.html is omitted, uses the input filename with .html extension.
"""
import json
import html
import sys
import os
from datetime import datetime


def escape(text):
    return html.escape(str(text))


def format_timestamp(ts):
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%H:%M:%S")
    except Exception:
        return ts[:19] if ts else ""


def format_date(ts):
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return ts[:10] if ts else ""


def extract_text_blocks(content):
    """Extract displayable content from message content."""
    blocks = []
    if isinstance(content, str):
        if content.strip().startswith(("<system-reminder>", "<task-notification>")):
            return blocks
        blocks.append(("text", content))
    elif isinstance(content, list):
        for item in content:
            if isinstance(item, str):
                blocks.append(("text", item))
            elif isinstance(item, dict):
                t = item.get("type", "")
                if t == "text":
                    text = item.get("text", "")
                    if text.strip().startswith(("<system-reminder>", "<task-notification>")):
                        continue
                    blocks.append(("text", text))
                elif t == "thinking":
                    blocks.append(("thinking", item.get("thinking", "")))
                elif t == "tool_use":
                    name = item.get("name", "unknown")
                    inp = item.get("input", {})
                    blocks.append(("tool_use", name, inp))
                elif t == "tool_result":
                    sub_content = item.get("content", "")
                    if isinstance(sub_content, list):
                        for sub in sub_content:
                            if isinstance(sub, dict) and sub.get("type") == "text":
                                text = sub.get("text", "")
                                if len(text) > 500:
                                    text = text[:500] + f"\n... ({len(text)} chars total)"
                                blocks.append(("tool_result", text))
                    elif isinstance(sub_content, str):
                        text = sub_content
                        if len(text) > 500:
                            text = text[:500] + f"\n... ({len(text)} chars total)"
                        blocks.append(("tool_result", text))
    return blocks


def render_tool_input(name, inp):
    """Render tool input in a compact way."""
    if name in ("Read", "read"):
        path = inp.get("file_path", "?")
        offset = inp.get("offset")
        limit = inp.get("limit")
        suffix = ""
        if offset or limit:
            suffix = f" (lines {offset or 1}-{(offset or 1) + (limit or 0)})"
        return f"Read: {path}{suffix}"
    elif name in ("Edit", "edit"):
        path = inp.get("file_path", "?")
        old = inp.get("old_string", "")[:80]
        return f"Edit: {path}\n  old: {old}..."
    elif name in ("Write", "write"):
        path = inp.get("file_path", "?")
        content = inp.get("content", "")
        return f"Write: {path} ({len(content)} chars)"
    elif name in ("Bash", "bash"):
        cmd = inp.get("command", "?")
        desc = inp.get("description", "")
        return f"{desc}\n$ {cmd}" if desc else f"$ {cmd}"
    elif name in ("Glob", "glob"):
        return f"Glob: {inp.get('pattern', '?')} in {inp.get('path', 'cwd')}"
    elif name in ("Grep", "grep"):
        return f"Grep: /{inp.get('pattern', '?')}/ in {inp.get('path', 'cwd')}"
    elif name == "Agent":
        desc = inp.get("description", "?")
        agent_type = inp.get("subagent_type", "general")
        return f"Agent: {desc} [{agent_type}]"
    elif name == "ToolSearch":
        return f"ToolSearch: {inp.get('query', '?')}"
    elif name == "Skill":
        return f"Skill: {inp.get('skill', '?')} {inp.get('args', '')}"
    elif name.startswith("mcp__claude-in-chrome__"):
        short = name.replace("mcp__claude-in-chrome__", "chrome:")
        action = inp.get("action", "")
        text = inp.get("text", "")
        coord = inp.get("coordinate", "")
        ref = inp.get("ref", "")
        parts = [short]
        if action:
            parts.append(action)
        if coord:
            parts.append(str(coord))
        if ref:
            parts.append(ref)
        if text:
            parts.append(f'"{text[:50]}"')
        return " ".join(parts)
    else:
        return f"{name}: {json.dumps(inp, ensure_ascii=False)[:200]}"


HTML_TEMPLATE_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Claude Code Transcript</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #1a1a2e; color: #e0e0e0; padding: 2rem; line-height: 1.6;
    max-width: 960px; margin: 0 auto;
  }
  h1 { color: #fbbf24; margin-bottom: 0.5rem; font-size: 1.5rem; }
  .subtitle { color: #888; margin-bottom: 2rem; font-size: 0.9rem; }
  .message {
    margin-bottom: 1rem; padding: 1rem 1.25rem; border-radius: 10px;
    border-left: 4px solid transparent; position: relative;
  }
  .message.user { background: #16213e; border-left-color: #3b82f6; }
  .message.assistant { background: #1e1e30; border-left-color: #fbbf24; }
  .role {
    font-size: 0.75rem; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.05em; margin-bottom: 0.4rem;
  }
  .role.user { color: #60a5fa; }
  .role.assistant { color: #fbbf24; }
  .timestamp { color: #666; font-size: 0.7rem; float: right; margin-top: 2px; }
  .text-block { white-space: pre-wrap; word-wrap: break-word; font-size: 0.9rem; }
  .thinking {
    background: #2a2a3e; border-radius: 6px; padding: 0.6rem 0.8rem;
    margin: 0.4rem 0; font-size: 0.8rem; color: #999;
    border-left: 3px solid #555; max-height: 120px; overflow-y: auto;
  }
  .thinking summary { cursor: pointer; color: #777; font-style: italic; }
  .tool-use {
    background: #1a2a1a; border-radius: 6px; padding: 0.6rem 0.8rem;
    margin: 0.4rem 0; font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 0.8rem; color: #86efac; border-left: 3px solid #22c55e;
    white-space: pre-wrap; word-wrap: break-word;
  }
  .tool-result {
    background: #2a2a20; border-radius: 6px; padding: 0.6rem 0.8rem;
    margin: 0.4rem 0; font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 0.75rem; color: #aaa; border-left: 3px solid #666;
    max-height: 150px; overflow-y: auto; white-space: pre-wrap; word-wrap: break-word;
  }
  .stats {
    color: #888; font-size: 0.8rem; margin-bottom: 1.5rem;
    padding: 0.8rem; background: #16213e; border-radius: 8px;
  }
  a { color: #60a5fa; }
  code {
    background: #2d2d44; padding: 1px 4px; border-radius: 3px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 0.85em;
  }
</style>
</head>
<body>
"""


def convert(input_path, output_path):
    entries = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not entries:
        print(f"Error: No valid JSON entries found in {input_path}", file=sys.stderr)
        sys.exit(1)

    parts = [HTML_TEMPLATE_HEAD]

    # Title from filename
    basename = os.path.splitext(os.path.basename(input_path))[0]
    full_path = os.path.abspath(input_path)
    parts.append(f"<h1>Claude Code Transcript</h1>")
    parts.append(f'<p class="subtitle">{escape(basename)}<br><small style="color:#666">Source: {escape(full_path)}</small></p>')

    # Stats
    user_msgs = sum(
        1 for e in entries if e.get("message", {}).get("role") == "user"
    )
    asst_msgs = sum(
        1 for e in entries if e.get("message", {}).get("role") == "assistant"
    )
    tool_uses = sum(
        1
        for e in entries
        if e.get("message", {}).get("role") == "assistant"
        and isinstance(e.get("message", {}).get("content"), list)
        and any(
            b.get("type") == "tool_use"
            for b in e["message"]["content"]
            if isinstance(b, dict)
        )
    )

    first_ts = entries[0].get("timestamp", "") if entries else ""
    last_ts = entries[-1].get("timestamp", "") if entries else ""

    parts.append('<div class="stats">')
    parts.append(
        f"<strong>Session:</strong> {format_date(first_ts)} "
        f"{format_timestamp(first_ts)} &mdash; {format_timestamp(last_ts)} "
        f"&nbsp;|&nbsp; <strong>Messages:</strong> {user_msgs} user, "
        f"{asst_msgs} assistant &nbsp;|&nbsp; "
        f"<strong>Tool calls:</strong> {tool_uses} &nbsp;|&nbsp; "
        f"<strong>Total entries:</strong> {len(entries)}"
    )
    parts.append("</div>")

    # Render messages
    msg_count = 0
    last_role = None

    for entry in entries:
        if entry.get("isSidechain"):
            continue

        msg = entry.get("message", {})
        role = msg.get("role", "")
        if role not in ("user", "assistant"):
            continue

        content = msg.get("content")
        blocks = extract_text_blocks(content)
        if not blocks:
            continue

        timestamp = format_timestamp(entry.get("timestamp", ""))

        if role != last_role:
            if last_role is not None:
                parts.append("</div>")
            msg_count += 1
            parts.append(f'<div class="message {role}" id="msg-{msg_count}">')
            parts.append(f'<span class="timestamp">{timestamp}</span>')
            parts.append(f'<div class="role {role}">{role}</div>')
            last_role = role

        for block in blocks:
            if block[0] == "text":
                text = block[1].strip()
                if not text:
                    continue
                parts.append(f'<div class="text-block">{escape(text)}</div>')
            elif block[0] == "thinking":
                thinking = block[1].strip()
                if not thinking:
                    continue
                short = thinking[:80].replace("\n", " ")
                parts.append(
                    f'<details class="thinking">'
                    f"<summary>Thinking: {escape(short)}...</summary>"
                    f"{escape(thinking)}</details>"
                )
            elif block[0] == "tool_use":
                rendered = render_tool_input(block[1], block[2])
                parts.append(f'<div class="tool-use">{escape(rendered)}</div>')
            elif block[0] == "tool_result":
                text = block[1].strip()
                if text:
                    parts.append(
                        f'<div class="tool-result">{escape(text)}</div>'
                    )

    if last_role is not None:
        parts.append("</div>")

    parts.append("</body></html>")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))

    input_size = os.path.getsize(input_path) / 1024
    output_size = os.path.getsize(output_path) / 1024
    reduction = (1 - output_size / input_size) * 100 if input_size > 0 else 0

    print(f"Converted {input_path} -> {output_path}")
    print(
        f"  {msg_count} message bubbles from {len(entries)} entries"
    )
    print(
        f"  {input_size:.0f} KB -> {output_size:.0f} KB "
        f"({reduction:.0f}% reduction)"
    )


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_transcript.py <input.jsonl> [output.html]")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = os.path.splitext(input_path)[0] + ".html"

    convert(input_path, output_path)


if __name__ == "__main__":
    main()
