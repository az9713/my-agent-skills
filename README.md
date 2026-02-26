# my-agent-skills

Fourteen personal skills for [Claude Code](https://claude.com/claude-code), plus an example audit report showing the skill-best-practices auditor in action.

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

### mcp-doctor

Diagnose and repair broken MCP server configurations across all known config sources. When MCP servers have broken paths, missing binaries, or unreachable endpoints, they cause EPIPE crashes that prevent Claude Code or omp from starting. This skill identifies the problem servers, disables them in the correct config file, and logs everything.

The script scans all known MCP config locations at both user and project levels: `~/.claude/mcp.json`, `~/.cursor/mcp.json`, `~/.codeium/windsurf/mcp_config.json`, `~/.omp/agent/mcp.json`, plus project-level equivalents and `.vscode/mcp.json`. For each server entry it verifies the command binary exists in `PATH` or at its absolute path, confirms Docker is running for `docker` commands, and validates absolute paths in arguments. Each server gets a status of OK, WARN (binary found but arg path missing), FAIL (binary not found), or SKIP (already disabled). On user confirmation, broken servers are disabled in their respective config file with a timestamped log written to `~/.claude/logs/`.

**Files:**
- `SKILL.md` — 5-step workflow (diagnose, review, fix, log, restart), status quick reference, common mistakes
- `scripts/mcp_doctor.sh` — Portable diagnostic script (bash + embedded node for JSON parsing and PATH lookup)

### repurpose

Repurpose any information source — lectures, papers, blog posts, transcripts, podcasts — into multiple high-quality derivative artifacts. Analyzes the source, proposes which artifact types fit, and generates them in parallel after user approval.

The skill uses a two-phase approach: first it classifies the source and checks for content signals (has quantitative data? has citations? is a presentation?), then it scores 13 possible artifact types as strong fit, moderate fit, or skip. The user reviews and approves the list before generation begins. This solves the problem of not all artifacts applying to all sources without needing rigid source-type rules.

**Artifact types:** Cheat Sheet (HTML), Key Numbers Card (HTML), Blog Post, Twitter Thread, Annotated Bibliography, Open Research Questions, Reproducibility Guide, Speaker Notes, Modular Outline, Q&A Prep, Diagram Pack (HTML), Executive Summary, Slide Deck Outline.

**Source types covered:** presentations/talks, academic papers, blog posts, YouTube transcripts, podcast transcripts, technical documentation, reports, interviews, book chapters.

**Files:**
- `SKILL.md` — 5-phase orchestration workflow (ingest, analyze, propose, generate, verify)
- `references/artifact-catalog.md` — 13 artifact types with include/skip criteria, structure templates, and quality gates
- `references/source-analysis-guide.md` — 9 source type profiles with extraction guidance
- `examples/example-run.md` — The Lambert talk run as a reference example

### llmbench

Full LLM benchmark pipeline — runs the same prompt across 4 models in parallel via OpenCode, then renders a 2x2 grid comparison video using Remotion.

**Files:**
- `SKILL.md` — Pipeline steps, model configuration, video rendering instructions

### code-review

Code review checklist and best practices for thorough quality assessment. Covers correctness, security, performance, readability, and maintainability dimensions.

**Files:**
- `SKILL.md` — Review checklist, severity classifications, common patterns

### debug-chrome-extension

Diagnose and fix Claude Code Chrome extension connection issues. Use when `/chrome` shows disabled status, MCP tools are unavailable, or browser automation fails to connect.

**Files:**
- `SKILL.md` — Diagnostic flowchart, common failure modes, resolution steps

### git-workflow

Git workflow patterns for branching, commits, and pull requests following project conventions.

**Files:**
- `SKILL.md` — Branching strategies, commit message conventions, PR workflow

### project-workflow

Project development workflow patterns including Plan-Build-Review-Fix cycle and feature development processes.

**Files:**
- `SKILL.md` — Development lifecycle phases, review gates, iteration patterns

### testing

Testing patterns, strategies, and best practices for comprehensive test coverage. Covers unit, integration, and end-to-end testing approaches.

**Files:**
- `SKILL.md` — Testing pyramid, coverage strategies, common patterns

### surveil

Launch a real-time surveillance dashboard for Claude Code agent teams. Monitors agent activity, task progress, and team coordination through a web-based dashboard.

**Files:**
- `SKILL.md` — Dashboard setup, monitoring configuration
- `server/` — Node.js server with SQLite storage, WebSocket updates, and web dashboard

**Setup:** Run `npm install` in `.claude/skills/surveil/server/` before first use.

### docker-windows

Run Docker containers on Windows with MINGW/MSYS2/Git Bash without silent path mangling, volume mount failures, or flag conversion issues.

The core problem: MINGW automatically converts anything that looks like a Unix path to a Windows path. `-w /work` becomes `-w C:/Program Files/Git/work`, volume mounts get rewritten, and single-letter flags like `-i` can be eaten by the conversion heuristic. These failures are **silent** — Docker starts but produces no output or wrong results. The fix is a single environment variable (`MSYS_NO_PATHCONV=1`) plus a consistent command pattern using `--entrypoint /bin/bash -c '...'`.

The skill covers the canonical Docker run pattern, a key-rules table, what-not-to-do examples, MOOSE-specific gotchas (JIT failures, renamed parameters, missing materials), and a 5-step debugging checklist for diagnosing silent failures.

**Files:**
- `SKILL.md` — Problem explanation, canonical patterns, MOOSE-specific section, debugging checklist (153 lines)

### moose-simulation

Full lifecycle skill for running MOOSE finite-element simulations on Windows via Docker. Covers prerequisites, input file authoring, Docker execution, output validation, visualization, and README documentation.

Built from lessons learned across 21 successful quickstart cases spanning framework kernels, heat transfer, solid mechanics, Navier-Stokes (finite volume), phase field, porous flow, and electromagnetics. The skill includes:

- **Prerequisites checklist**: Docker Desktop running, `idaholab/moose:latest` image available, input file validated
- **Input file standards**: naming conventions, header comment blocks, inline comments, required output blocks, mesh sizing guidelines, Docker portability rules (JIT, parameter renames)
- **Docker execution**: canonical run command with every element explained, success/failure indicators, batch run pattern
- **Output validation**: required artifacts (`.e` + `.csv`), CSV sanity checks, Exodus field verification
- **Visualization**: nodal vs element variables, FV (finite volume) handling, multi-block mesh concatenation, plot naming conventions
- **README template**: physics explanation, input file walkthrough, Docker command, expected results, key takeaways
- **7 common failure patterns** with exact fixes: path mangling, JIT compilation, PorousFlow materials, renamed parameters, FV parameter names, solver divergence, porosity type
- **Physics module quick reference** table mapping modules to cases and key MOOSE objects
- **10-step workflow checklist** for creating a new simulation from scratch

**Files:**
- `SKILL.md` — 9 sections, 10-step checklist, 466 lines

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
# All skills
cp -r .claude/skills/* ~/.claude/skills/

# Or individually
cp -r .claude/skills/windows-desktop ~/.claude/skills/
cp -r .claude/skills/surveil ~/.claude/skills/
# ... etc
```

For the `surveil` skill, also run:
```bash
cd ~/.claude/skills/surveil/server && npm install
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
/mcp-doctor               # Diagnose and fix broken MCP servers
/code-review              # Run code review checklist
/debug-chrome-extension   # Fix Chrome extension issues
/git-workflow             # Git branching and PR patterns
/project-workflow         # Plan-Build-Review-Fix cycle
/testing                  # Testing strategies and patterns
/surveil                  # Launch agent team dashboard
/docker-windows           # Docker on Windows without path mangling
/moose-simulation         # Run MOOSE simulations via Docker
```
