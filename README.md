# my-agent-skills

Four personal skills for [Claude Code](https://claude.com/claude-code), plus an example audit report showing the skill-best-practices auditor in action.

## Skills

### windows-desktop

Control the Windows desktop through PowerShell commands. Covers 16 operation categories — window management, app launching, screenshots, volume control, system info, network info, file browsing, virtual desktops, clipboard, keyboard/mouse input, notifications, and more.

All file and directory operations are **strictly read-only**. The skill enforces a comprehensive prohibited-commands list that blocks file writes, process kills, shutdowns, registry writes, service control, network changes, firewall rules, and scheduled tasks. The only file-creation exception is screenshots (saved to `%TEMP%`).

**Files:**
- `SKILL.md` — Safety rules, operation category overview, quick-reference PowerShell snippets, common mistakes
- `powershell-reference.md` — Full command reference for all 16 categories with copy-paste-ready snippets (569 lines)

### plugin-skill-auditor

Inventory all personal Claude Code skills and plugin marketplaces, create a full backup, and generate a comprehensive report with exact removal and restoration instructions for every item.

This skill is **audit and backup only** — it never deletes, removes, or modifies anything. It scans `~/.claude/skills/`, `~/.claude/plugins/marketplaces/`, `~/.claude/plugins/cache/`, and `~/.claude/settings.json`, then writes an `AUDIT-REPORT.md` with per-item removal commands, restoration commands, a nuclear-option cleanup script, and a full restoration procedure.

**Files:**
- `SKILL.md` — Scope definition, 5-step execution procedure, report section templates, safety constraints

### skill-best-practices

Audit installed Claude Code skills against a 25-check best-practices checklist and output ranked findings to the terminal. Accepts an optional skill name or audits all personal skills by default.

The 25 checks are organized by severity:

| Severity | Checks | Points each | What they catch |
|----------|--------|-------------|-----------------|
| Critical (C01-C04) | 4 | 8 | Missing SKILL.md, missing frontmatter, missing `name`/`description` |
| High (H01-H06) | 6 | 4 | No "Use when" triggers in description, SKILL.md over 500 lines, unreferenced files, invalid name format, folder/name mismatch |
| Medium (M01-M10) | 10 | 2 | No `allowed-tools`, verbose body without `references/`, extraneous docs, non-standard frontmatter fields, deep nesting, missing TOC in long references, side-effect skills without safety flags |
| Low (L01-L05) | 5 | 1 | Passive voice, description length, missing common-mistakes section, keyword stuffing |

Scores are calculated as earned points out of 81 maximum (Critical=32 + High=24 + Medium=20 + Low=5).

**Where the best practices come from:**
1. [Anthropic's official Claude Code skills documentation](https://code.claude.com/docs/en/skills) — file format, supported frontmatter fields, directory conventions, progressive disclosure pattern
2. Anthropic's `skill-creator` guide (from the `anthropic-agent-skills` marketplace) — Claude Search Optimization (CSO), description writing, naming conventions, token efficiency

**Files:**
- `SKILL.md` — Execution steps, output format specification, edge cases
- `references/checklist.md` — All 25 checks with IDs, detection logic, fix recommendations, and scoring weights

### repurpose

Repurpose any information source — lectures, papers, blog posts, transcripts, podcasts — into multiple high-quality derivative artifacts. Analyzes the source, proposes which artifact types fit, and generates them in parallel after user approval.

The skill uses a two-phase approach: first it classifies the source and checks for content signals (has quantitative data? has citations? is a presentation?), then it scores 13 possible artifact types as strong fit, moderate fit, or skip. The user reviews and approves the list before generation begins. This solves the problem of not all artifacts applying to all sources without needing rigid source-type rules.

**Artifact types:** Cheat Sheet (HTML), Key Numbers Card (HTML), Blog Post, Twitter Thread, Annotated Bibliography, Open Research Questions, Reproducibility Guide, Speaker Notes, Modular Outline, Q&A Prep, Diagram Pack (HTML), Executive Summary, Slide Deck Outline.

**Source types covered:** presentations/talks, academic papers, blog posts, YouTube transcripts, podcast transcripts, technical documentation, reports, interviews, book chapters.

Built from the experience of repurposing Nathan Lambert's 113-slide CMU talk "Building Olmo in the Era of Agents" into 11 artifacts. See the full story at [az9713/claude-repurpose-talk](https://github.com/az9713/claude-repurpose-talk).

**Files:**
- `SKILL.md` — 5-phase orchestration workflow (ingest, analyze, propose, generate, verify)
- `references/artifact-catalog.md` — 13 artifact types with include/skip criteria, structure templates, and quality gates
- `references/source-analysis-guide.md` — 9 source type profiles with extraction guidance
- `examples/example-run.md` — The Lambert talk run as a reference example

## Outputs

### outputs/skill-audit-report.md

A sample audit report generated by running `skill-best-practices` against 15 personal skills. Each skill gets a detailed table showing every check as PASS or FAIL, with fix recommendations for failures. The report ends with:

- **Summary table** — per-skill fail counts by severity and weighted score percentage
- **Stats** — 15 skills audited, 93% average score, 0 critical failures, 1 perfect score (windows-desktop at 100%)
- **Issue frequency** — M01 (no `allowed-tools` restriction) was the most common issue, affecting 10 of 15 skills
- **Scoring methodology** — weighted point system explained

## Installation

Copy the skills you want into your personal skills directory:

```bash
# All four
cp -r .claude/skills/* ~/.claude/skills/

# Or individually
cp -r .claude/skills/windows-desktop ~/.claude/skills/
cp -r .claude/skills/plugin-skill-auditor ~/.claude/skills/
cp -r .claude/skills/skill-best-practices ~/.claude/skills/
cp -r .claude/skills/repurpose ~/.claude/skills/
```

Restart Claude Code for the skills to take effect.

## Usage

Skills activate automatically when Claude detects a matching request, or can be invoked directly:

```
/windows-desktop          # Activates for Windows desktop operations
/plugin-skill-auditor     # Backup and audit all skills/plugins
/skill-best-practices     # Audit all skills against best practices
/skill-best-practices windows-desktop   # Audit a single skill
/repurpose slides.pdf     # Repurpose a source into multiple artifacts
/repurpose https://arxiv.org/abs/2501.12345  # Works with URLs too
```
