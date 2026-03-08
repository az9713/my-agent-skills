#!/usr/bin/env python3
"""Convert Codex session JSONL transcript to readable HTML.

Usage:
    python convert_codex_transcript.py <input.jsonl> [output.html]
"""

from __future__ import annotations

import html
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Any


MAX_TOOL_OUTPUT_CHARS = 3000
MAX_TOOL_ARGS_CHARS = 2500


@dataclass
class TimelineItem:
    kind: str  # message | tool_call | tool_output | note
    timestamp: str
    role: str = ""
    text: str = ""
    call_name: str = ""
    call_id: str = ""
    args: str = ""


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value))


def format_ts(ts: str) -> str:
    if not ts:
        return ""
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%H:%M:%S")
    except Exception:
        return ts[:19]


def format_date(ts: str) -> str:
    if not ts:
        return ""
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return ts[:10]


def pretty_json_or_text(raw: Any, limit: int) -> str:
    if raw is None:
        return ""
    if isinstance(raw, (dict, list)):
        s = json.dumps(raw, ensure_ascii=False, indent=2)
    else:
        s = str(raw)
        stripped = s.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            try:
                parsed = json.loads(stripped)
                s = json.dumps(parsed, ensure_ascii=False, indent=2)
            except Exception:
                pass
    if len(s) > limit:
        s = s[:limit] + f"\n... ({len(str(raw))} chars total)"
    return s


def extract_message_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content.strip()
    if not isinstance(content, list):
        return str(content).strip()

    chunks: list[str] = []
    for item in content:
        if isinstance(item, str):
            t = item.strip()
            if t:
                chunks.append(t)
            continue
        if not isinstance(item, dict):
            continue
        tpe = item.get("type")
        if tpe in {"output_text", "input_text", "text"}:
            txt = item.get("text") or item.get("input_text") or item.get("output_text") or ""
            txt = str(txt).strip()
            if txt:
                chunks.append(txt)
        elif tpe == "tool_result":
            txt = pretty_json_or_text(item.get("content", ""), MAX_TOOL_OUTPUT_CHARS // 2).strip()
            if txt:
                chunks.append(f"[tool_result]\n{txt}")
    return "\n\n".join(chunks).strip()


def should_skip_message(role: str, text: str, include_system: bool = False) -> bool:
    if role in {"developer", "system"} and not include_system:
        return True
    if not text.strip():
        return True
    lower = text.lower()
    if lower.startswith("<system-reminder>") or lower.startswith("<task-notification>"):
        return True
    return False


def parse_timeline(entries: list[dict[str, Any]], include_system: bool = False) -> tuple[list[TimelineItem], dict[str, Any]]:
    timeline: list[TimelineItem] = []
    calls_by_id: dict[str, dict[str, str]] = {}

    role_counts = {"user": 0, "assistant": 0, "developer": 0, "system": 0}
    tool_call_count = 0
    tool_output_count = 0

    for e in entries:
        ts = format_ts(e.get("timestamp", ""))
        typ = e.get("type", "")
        payload = e.get("payload", {}) if isinstance(e.get("payload"), dict) else {}

        if typ != "response_item":
            continue

        ptype = payload.get("type", "")

        if ptype == "message":
            role = payload.get("role", "assistant")
            text = extract_message_text(payload.get("content"))
            if should_skip_message(role, text, include_system=include_system):
                continue
            role_counts[role] = role_counts.get(role, 0) + 1
            timeline.append(TimelineItem(kind="message", timestamp=ts, role=role, text=text))
            continue

        if ptype in {"function_call", "custom_tool_call", "web_search_call"}:
            name = payload.get("name") or ("web_search" if ptype == "web_search_call" else ptype)
            call_id = payload.get("call_id", "")
            args_raw = payload.get("arguments", payload.get("input", payload.get("action", {})))
            args = pretty_json_or_text(args_raw, MAX_TOOL_ARGS_CHARS)
            if call_id:
                calls_by_id[call_id] = {"name": str(name)}
            tool_call_count += 1
            timeline.append(
                TimelineItem(
                    kind="tool_call",
                    timestamp=ts,
                    call_name=str(name),
                    call_id=str(call_id),
                    args=args,
                )
            )
            continue

        if ptype in {"function_call_output", "custom_tool_call_output"}:
            call_id = str(payload.get("call_id", ""))
            output = pretty_json_or_text(payload.get("output", ""), MAX_TOOL_OUTPUT_CHARS)
            name = calls_by_id.get(call_id, {}).get("name", "tool")
            tool_output_count += 1
            timeline.append(
                TimelineItem(
                    kind="tool_output",
                    timestamp=ts,
                    call_name=name,
                    call_id=call_id,
                    text=output,
                )
            )
            continue

    stats = {
        "role_counts": role_counts,
        "tool_calls": tool_call_count,
        "tool_outputs": tool_output_count,
    }
    return timeline, stats


def load_entries(input_path: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def render_html(input_path: str, entries: list[dict[str, Any]], timeline: list[TimelineItem], stats: dict[str, Any]) -> str:
    first_ts = entries[0].get("timestamp", "") if entries else ""
    last_ts = entries[-1].get("timestamp", "") if entries else ""
    basename = os.path.splitext(os.path.basename(input_path))[0]

    parts: list[str] = []
    parts.append("<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>")
    parts.append(f"<title>Codex Transcript - {esc(basename)}</title>")
    parts.append(
        "<style>body{font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#111827;color:#e5e7eb;max-width:1000px;margin:0 auto;padding:20px}h1{color:#f59e0b}pre{white-space:pre-wrap;word-wrap:break-word} .stats{background:#1f2937;padding:12px;border-radius:8px;margin:10px 0 20px} .item{padding:12px;border-radius:10px;margin:10px 0;border-left:4px solid transparent} .user{background:#1e3a8a;border-left-color:#60a5fa} .assistant{background:#292524;border-left-color:#f59e0b} .developer{background:#3f3f46;border-left-color:#a78bfa} .toolcall{background:#052e16;border-left-color:#22c55e} .toolout{background:#1f2937;border-left-color:#9ca3af} .meta{font-size:12px;color:#9ca3af;margin-bottom:6px} code{background:#374151;padding:2px 4px;border-radius:4px}</style>"
    )
    parts.append("</head><body>")
    parts.append(f"<h1>Codex Session Transcript</h1><div>Session: <code>{esc(basename)}</code></div>")
    parts.append(f"<div class='stats'><b>Date:</b> {esc(format_date(first_ts))} &nbsp; <b>Time:</b> {esc(format_ts(first_ts))} - {esc(format_ts(last_ts))} &nbsp; <b>Entries:</b> {len(entries)} &nbsp; <b>Bubbles:</b> {len(timeline)} &nbsp; <b>User:</b> {stats['role_counts'].get('user',0)} &nbsp; <b>Assistant:</b> {stats['role_counts'].get('assistant',0)} &nbsp; <b>Tool calls:</b> {stats.get('tool_calls',0)}</div>")

    for item in timeline:
        if item.kind == "message":
            role_class = item.role if item.role in {"user", "assistant", "developer"} else "assistant"
            parts.append(f"<div class='item {role_class}'><div class='meta'>{esc(item.role.upper())} · {esc(item.timestamp)}</div><pre>{esc(item.text)}</pre></div>")
        elif item.kind == "tool_call":
            cid = f" ({item.call_id})" if item.call_id else ""
            parts.append(f"<div class='item toolcall'><div class='meta'>TOOL CALL · {esc(item.timestamp)}</div><div><b>{esc(item.call_name)}</b>{esc(cid)}</div><pre>{esc(item.args)}</pre></div>")
        elif item.kind == "tool_output":
            cid = f" ({item.call_id})" if item.call_id else ""
            parts.append(f"<div class='item toolout'><div class='meta'>TOOL OUTPUT · {esc(item.timestamp)}</div><div><b>{esc(item.call_name)}</b>{esc(cid)}</div><pre>{esc(item.text)}</pre></div>")

    parts.append("</body></html>")
    return "\n".join(parts)


def convert(input_path: str, output_path: str, include_system: bool = False) -> None:
    entries = load_entries(input_path)
    if not entries:
        raise ValueError(f"No valid JSON entries found in {input_path}")

    timeline, stats = parse_timeline(entries, include_system=include_system)
    html_out = render_html(input_path, entries, timeline, stats)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_out)

    in_kb = os.path.getsize(input_path) / 1024
    out_kb = os.path.getsize(output_path) / 1024
    reduction = (1 - (out_kb / in_kb)) * 100 if in_kb else 0

    print(f"Converted {input_path} -> {output_path}")
    print(f"  {len(timeline)} timeline items from {len(entries)} entries")
    print(f"  {stats['role_counts'].get('user',0)} user, {stats['role_counts'].get('assistant',0)} assistant messages")
    print(f"  {stats.get('tool_calls',0)} tool calls, {stats.get('tool_outputs',0)} tool outputs")
    print(f"  {in_kb:.0f} KB -> {out_kb:.0f} KB ({reduction:.0f}% reduction)")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python convert_codex_transcript.py <input.jsonl> [output.html] [--include-system]")
        return 1

    include_system = "--include-system" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--include-system"]
    input_path = args[0]

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found", file=sys.stderr)
        return 1

    if len(args) >= 2:
        output_path = args[1]
    else:
        output_path = os.path.splitext(input_path)[0] + ".html"

    try:
        convert(input_path, output_path, include_system=include_system)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

