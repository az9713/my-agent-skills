---
name: codex-transcript-to-html
description: Convert Codex session JSONL transcript files into readable HTML with conversation bubbles and tool-call timelines. Use this whenever a user asks to export a Codex session, make a .jsonl session readable/shareable, or convert Codex transcript/session logs to HTML.
---

# Codex Transcript to HTML

Convert Codex session `.jsonl` logs into readable, styled HTML.

## Use cases

- "convert this Codex session jsonl to html"
- "make this transcript readable"
- "export/share this Codex session"

## Run

If `CODEX_HOME` is set:

```bash
python "$CODEX_HOME/skills/codex-transcript-to-html/scripts/convert_codex_transcript.py" <input.jsonl> <output.html>
```

If `CODEX_HOME` is not set (default location):

```bash
python ~/.codex/skills/codex-transcript-to-html/scripts/convert_codex_transcript.py <input.jsonl> <output.html>
```

Windows PowerShell:

```powershell
python "$env:USERPROFILE\.codex\skills\codex-transcript-to-html\scripts\convert_codex_transcript.py" <input.jsonl> <output.html>
```

If output path is omitted, output defaults to input filename with `.html`.

## What this converter understands

- `response_item` message payloads (user/assistant/developer/system)
- `response_item` function/custom tool calls
- corresponding function/custom tool call outputs
- basic web search call events

The converter filters noise by default and focuses on user/assistant conversation plus tool timeline.

## Output expectations

After running, return:
1. Output HTML file path
2. High-level stats reported by the converter (entries parsed, bubbles, tool calls)

