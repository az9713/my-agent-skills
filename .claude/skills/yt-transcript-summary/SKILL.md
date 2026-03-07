---
name: yt-transcript-summary
description: Analyze YouTube videos or local transcript files using Google Gemini API. Extracts key takeaways, summaries, code, prompts, and more.
triggers:
  - summarize youtube video
  - summarize youtube
  - summarize transcript
  - analyze youtube
  - analyze video
  - yt summary
  - yt transcript
  - youtube takeaways
  - extract from video
---

# YouTube Transcript & Video Analyzer

Analyze YouTube videos or local transcript files using Google Gemini API via the `yt_analyze.py` CLI tool.

## Script Location

`C:\Users\simon\Downloads\colab_to_script\yt_analyze.py`

## How to Build the Command

Parse the user's request for these inputs:

| Input | How to pass it |
|-------|---------------|
| YouTube URL | Positional argument: `python yt_analyze.py "URL"` |
| Local file path | `--file "path/to/file.txt"` |
| Custom prompt (inline text) | `-p "prompt text"` |
| Built-in preset | `--builtin <preset>` |
| Transcript mode | `--transcript` (optionally `--speakers "Name1" "Name2"`) |
| Segment analysis | `--start MM:SS --end MM:SS` |
| Custom output path | `-o "output.md"` |

**URL and `--file` are mutually exclusive** — the script enforces this.

## Prompt Resolution Order

1. If the user says "transcript mode" or wants a transcript → use `--transcript`
2. If the user names a built-in preset → use `--builtin <preset>`
3. If the user provides an inline prompt → use `-p "their prompt"`
4. Otherwise → omit prompt flags (the script defaults to reading `my_prompt.txt`)

### Available Built-in Presets

`summary`, `summary-full`, `summarize-tests`, `takeaways`, `extract-code`, `extract-python`, `extract-notebook-code`, `extract-notebook-cells`, `extract-prompts`, `extract-system-prompts`, `extract-markdown`, `extract-markdown-contents`, `extract-source-and-markdown`, `extract-text`, `extract-commands`, `extract-terminal`, `extract-slides`, `extract-prompts-and-responses`, `extract-all`, `extract-task-instructions`, `extract-skills`, `extract-agentic-prompts`, `extract-claude-md`, `extract-prd`, `extract-workflow-md`, `extract-settings-json`, `extract-spec-md`, `extract-imagen-prompts`, `extract-veo-prompts`, `extract-music-prompts`, `extract-pipeline-yaml`, `extract-input-text`, `extract-tree-view`, `extract-workflow`

## Execution

Run the command via `Bash` from the script's directory:

```bash
cd /c/Users/simon/Downloads/colab_to_script && python yt_analyze.py <args>
```

The script writes output to an auto-named `.md` file and prints the path to stderr. After execution, tell the user the output file path.

## Examples

**YouTube URL with default prompt:**
```bash
cd /c/Users/simon/Downloads/colab_to_script && python yt_analyze.py "https://www.youtube.com/watch?v=abc123"
```

**Local transcript file:**
```bash
cd /c/Users/simon/Downloads/colab_to_script && python yt_analyze.py --file "/path/to/transcript.txt"
```

**Custom inline prompt:**
```bash
cd /c/Users/simon/Downloads/colab_to_script && python yt_analyze.py "https://www.youtube.com/watch?v=abc123" -p "Extract all code snippets"
```

**Built-in preset:**
```bash
cd /c/Users/simon/Downloads/colab_to_script && python yt_analyze.py "https://www.youtube.com/watch?v=abc123" --builtin takeaways
```

**Transcript mode with speakers:**
```bash
cd /c/Users/simon/Downloads/colab_to_script && python yt_analyze.py "https://www.youtube.com/watch?v=abc123" --transcript --speakers "Alice" "Bob"
```

**Segment analysis:**
```bash
cd /c/Users/simon/Downloads/colab_to_script && python yt_analyze.py "https://www.youtube.com/watch?v=abc123" --start 01:30 --end 05:00 -p "Summarize this segment"
```

## Prerequisites

- `GOOGLE_API_KEY` must be set (in `.env` or environment)
- `yt-dlp` must be installed (for fetching video metadata/titles)
- Python dependencies: `pip install -r requirements.txt` (google-genai, python-dotenv, jinja2)
