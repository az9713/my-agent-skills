# Skill Best Practices Audit Report

**Date:** 2026-02-13
**Scope:** All personal skills in `~/.claude/skills/` (excluding `skill-best-practices`)
**Skills audited:** 15
**Checklist:** 25 checks (4 Critical, 6 High, 10 Medium, 5 Low)

---

## agent-browser

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | Description contains "Use when" triggers |
| High | H02 | PASS | 279 lines (< 500) |
| High | H03 | PASS | All references/ and templates/ files linked from SKILL.md |
| High | H04 | PASS | Name `agent-browser` matches format |
| High | H05 | PASS | Folder matches name field |
| High | H06 | PASS | Folder uses kebab-case |
| Medium | M01 | PASS | Has `allowed-tools: Bash(agent-browser:*)` |
| Medium | M02 | PASS | Has references/ directory |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | PASS | Standard fields only |
| Medium | M05 | PASS | No deep nesting |
| Medium | M06 | PASS | Reference files present |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task skill |
| Medium | M09 | PASS | No `$ARGUMENTS` used |
| Medium | M10 | PASS | No duplicated content |
| Low | L01 | PASS | Imperative form ("Navigate", "Snapshot", "Interact") |
| Low | L02 | **FAIL** | Description ~500 chars (ideal: 20-300) |
| Low | L03 | PASS | Not background knowledge |
| Low | L04 | **FAIL** | No "Common Mistakes" or "Troubleshooting" heading |
| Low | L05 | **FAIL** | Description exceeds 500 chars (keyword stuffing) |

**Fixes:**
- L02/L05: Trim description to essential triggering conditions. Move trigger examples into SKILL.md body.
- L04: Add a section documenting common mistakes and their fixes.

**Passed:** 22/25 — **Score: 96%**

---

## browser-use

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | Description contains "Use when" triggers |
| High | H02 | **FAIL** | 857 lines (max 500) |
| High | H03 | PASS | No supporting files to check |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | PASS | Has `allowed-tools` |
| Medium | M02 | **FAIL** | 857 lines with no references/ directory |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | PASS | Standard fields only |
| Medium | M05 | PASS | No subdirectories |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | Description ~220 chars |
| Low | L03 | PASS | Not background knowledge |
| Low | L04 | PASS | Has "Troubleshooting" section |
| Low | L05 | PASS | Description under 500 chars |

**Fixes:**
- H02/M02: Move heavy reference content (commands, subagents, remote mode, profiles) to `references/` files and link from SKILL.md.

**Passed:** 23/25 — **Score: 93%**

---

## code-review

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | **FAIL** | Description lacks "use when" trigger phrases |
| High | H02 | PASS | 221 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard field `triggers:` in frontmatter |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form in checklists |
| Low | L02 | PASS | ~75 chars |
| Low | L03 | PASS | Has step-based instructions |
| Low | L04 | PASS | Has "Common Issues to Catch" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- H01: Rewrite description to start with "Use when reviewing code for quality, security, or correctness issues..."
- M01: Add `allowed-tools: Read, Glob, Grep` to frontmatter.
- M04: Remove `triggers:` field. Use `description` keywords for discoverability instead.

**Passed:** 22/25 — **Score: 90%**

---

## debug-chrome-extension

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | "Use when /chrome shows disabled status..." |
| High | H02 | PASS | 217 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | PASS | Standard fields only |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | ~170 chars |
| Low | L03 | PASS | Not background knowledge |
| Low | L04 | PASS | Has "Common Failure Modes" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- M01: Add `allowed-tools: Bash, Read, Grep` to frontmatter.

**Passed:** 24/25 — **Score: 98%**

---

## find-skills

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | Description has trigger phrases |
| High | H02 | PASS | 133 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | PASS | Standard fields only |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | ~250 chars |
| Low | L03 | PASS | Not background knowledge |
| Low | L04 | **FAIL** | No "Common Mistakes" or "Troubleshooting" heading |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- M01: Add `allowed-tools: Bash` to frontmatter.
- L04: Add a troubleshooting section for common search failures.

**Passed:** 23/25 — **Score: 96%**

---

## git-workflow

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | **FAIL** | Description lacks "use when" trigger phrases |
| High | H02 | PASS | 268 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard field `triggers:` in frontmatter |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | ~90 chars |
| Low | L03 | PASS | Has step-based instructions |
| Low | L04 | PASS | Has "Troubleshooting" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- H01: Rewrite description to start with "Use when branching, committing, or creating pull requests..."
- M01: Add `allowed-tools: Bash` to frontmatter.
- M04: Remove `triggers:` field. Use `description` keywords instead.

**Passed:** 22/25 — **Score: 90%**

---

## plugin-skill-auditor

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | "Use when you want to inventory, backup, or prepare to clean up" |
| High | H02 | PASS | 262 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | PASS | Has `allowed-tools` |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | PASS | Standard fields only |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a destructive side-effect skill |
| Medium | M08 | PASS | Not a long-running forked task |
| Medium | M09 | PASS | Has `$ARGUMENTS` and `argument-hint` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | **FAIL** | Description ~420 chars (ideal: 20-300) |
| Low | L03 | PASS | Not background knowledge |
| Low | L04 | PASS | Has "Important Constraints" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- L02: Trim scope clarifications into the SKILL.md body. Keep description under 300 chars.

**Passed:** 24/25 — **Score: 99%**

---

## project-workflow

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | **FAIL** | Description lacks "use when" trigger phrases |
| High | H02 | PASS | 268 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard field `triggers:` in frontmatter |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | ~115 chars |
| Low | L03 | PASS | Has step-based instructions |
| Low | L04 | PASS | Has "Workflow Troubleshooting" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- H01: Start description with "Use when following the Plan-Build-Review-Fix development cycle..."
- M01: Add `allowed-tools:` to frontmatter.
- M04: Remove `triggers:` field.

**Passed:** 22/25 — **Score: 90%**

---

## surveil

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | **FAIL** | Description lacks "use when" trigger phrases |
| High | H02 | PASS | 49 lines (< 500) |
| High | H03 | PASS | Server files referenced via directory path |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | PASS | Has `allowed-tools: - Bash` |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard field `triggers:` in frontmatter |
| Medium | M05 | **FAIL** | Deeply nested: `server/data/`, `server/lib/`, `server/public/` (>1 level) |
| Medium | M06 | PASS | No reference files in references/ |
| Medium | M07 | PASS | Not a destructive side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form ("Check if", "Start the server") |
| Low | L02 | PASS | ~70 chars |
| Low | L03 | PASS | Not background knowledge |
| Low | L04 | **FAIL** | No "Common Mistakes" or "Troubleshooting" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- H01: Rewrite as "Use when you want to monitor Claude Code agent teams in real-time..."
- M04: Remove `triggers:` field.
- M05: Flatten directory structure if possible, or accept as necessary for the server application.
- L04: Add troubleshooting section (e.g., port conflicts, missing node_modules).

**Passed:** 21/25 — **Score: 89%**

---

## testing

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | **FAIL** | Description lacks "use when" trigger phrases |
| High | H02 | PASS | 359 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | **FAIL** | 359 lines with no references/ directory |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard field `triggers:` in frontmatter |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | ~80 chars |
| Low | L03 | PASS | Has step-based instructions |
| Low | L04 | **FAIL** | No "Common Mistakes" heading |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- H01: Start description with "Use when writing tests, planning test coverage, or applying testing patterns..."
- M01: Add `allowed-tools: Read, Glob, Grep` for a reference skill.
- M02: Extract code examples into `references/` files.
- M04: Remove `triggers:` field.
- L04: Add a "Common Mistakes" section covering over-mocking, shared state, etc.

**Passed:** 20/25 — **Score: 86%**

---

## ui-ux-pro-max

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | Description contains extensive action triggers |
| High | H02 | PASS | 386 lines (< 500) |
| High | H03 | PASS | No supporting files in directory |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | **FAIL** | 386 lines with no references/ directory |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | PASS | Standard fields only |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | **FAIL** | Has Step 1/2/3/4 patterns but no `context: fork` |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | **FAIL** | Description ~800+ chars (ideal: 20-300) |
| Low | L03 | PASS | Has step-based instructions |
| Low | L04 | PASS | Has "Common Rules for Professional UI" section |
| Low | L05 | **FAIL** | Description exceeds 500 chars (keyword stuffing) |

**Fixes:**
- M01: Add `allowed-tools: Bash, Read, Glob` to frontmatter.
- M02: Move CSV data tables and rule databases into `references/` files.
- M08: Consider adding `context: fork` for long-running design system generation.
- L02/L05: Drastically trim description to triggering conditions only. Move keyword lists into SKILL.md body.

**Passed:** 20/25 — **Score: 90%**

---

## vercel-react-best-practices

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | "should be used when writing, reviewing, or refactoring" |
| High | H02 | PASS | 136 lines (< 500) |
| High | H03 | PASS | No supporting files in directory |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard fields: `license:`, `metadata:` |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | **FAIL** | Description ~310 chars (ideal: 20-300) |
| Low | L03 | PASS | Has "How to Use" section |
| Low | L04 | **FAIL** | No "Common Mistakes" or "Troubleshooting" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- M01: Add `allowed-tools: Read, Glob, Grep`.
- M04: Remove `license:` and `metadata:` from frontmatter.
- L02: Trim description slightly to fit under 300 chars.
- L04: Add a common pitfalls section.

**Passed:** 21/25 — **Score: 93%**

---

## vercel-react-native-skills

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | "Use when building React Native components" |
| High | H02 | PASS | 121 lines (< 500) |
| High | H03 | PASS | No supporting files in directory |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard fields: `license:`, `metadata:` |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | ~260 chars |
| Low | L03 | PASS | Has "How to Use" section |
| Low | L04 | **FAIL** | No "Common Mistakes" or "Troubleshooting" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- M01: Add `allowed-tools: Read, Glob, Grep`.
- M04: Remove `license:` and `metadata:` from frontmatter.
- L04: Add a section covering common React Native pitfalls.

**Passed:** 22/25 — **Score: 94%**

---

## web-design-guidelines

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | "Use when asked to..." |
| High | H02 | PASS | 39 lines (< 500) |
| High | H03 | PASS | No supporting files |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | **FAIL** | No `allowed-tools` restriction |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | **FAIL** | Non-standard field `metadata:` (with nested author, version, argument-hint) |
| Medium | M05 | PASS | No nesting |
| Medium | M06 | PASS | No reference files |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form ("Fetch", "Read", "Check", "Output") |
| Low | L02 | PASS | ~195 chars |
| Low | L03 | PASS | Has steps |
| Low | L04 | **FAIL** | No "Common Mistakes" or "Troubleshooting" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:**
- M01: Add `allowed-tools: Read, WebFetch, Glob, Grep`.
- M04: Move `argument-hint` to top-level frontmatter. Remove `metadata:`, `author:`, `version:`.
- L04: Add a section with common Web Interface Guidelines violations.

**Passed:** 22/25 — **Score: 94%**

---

## windows-desktop

| Criticality | ID | Status | Detail |
|---|---|---|---|
| Critical | C01 | PASS | SKILL.md exists |
| Critical | C02 | PASS | YAML frontmatter present |
| Critical | C03 | PASS | `name` field present |
| Critical | C04 | PASS | `description` field present |
| High | H01 | PASS | "Use when performing Windows Desktop operations..." |
| High | H02 | PASS | 135 lines (< 500) |
| High | H03 | PASS | powershell-reference.md referenced in SKILL.md |
| High | H04 | PASS | Name format valid |
| High | H05 | PASS | Folder matches name |
| High | H06 | PASS | Kebab-case |
| Medium | M01 | PASS | Has `allowed-tools` |
| Medium | M02 | PASS | Under 300 lines |
| Medium | M03 | PASS | No extraneous docs |
| Medium | M04 | PASS | Standard fields only |
| Medium | M05 | PASS | No deep nesting |
| Medium | M06 | PASS | No reference files in references/ |
| Medium | M07 | PASS | Not a side-effect skill |
| Medium | M08 | PASS | Not a multi-step task |
| Medium | M09 | PASS | No `$ARGUMENTS` |
| Medium | M10 | PASS | No duplication |
| Low | L01 | PASS | Imperative form |
| Low | L02 | PASS | ~175 chars |
| Low | L03 | PASS | Has step-based instructions |
| Low | L04 | PASS | Has "Common Mistakes to Avoid" section |
| Low | L05 | PASS | Under 500 chars |

**Fixes:** None needed.

**Passed:** 25/25 — **Score: 100%**

---

## Summary

| Skill | Critical | High | Medium | Low | Passed | Score% |
|-------|----------|------|--------|-----|--------|--------|
| agent-browser | 0 | 0 | 0 | 3 | 22/25 | 96% |
| browser-use | 0 | 1 | 1 | 0 | 23/25 | 93% |
| code-review | 0 | 1 | 2 | 0 | 22/25 | 90% |
| debug-chrome-extension | 0 | 0 | 1 | 0 | 24/25 | 98% |
| find-skills | 0 | 0 | 1 | 1 | 23/25 | 96% |
| git-workflow | 0 | 1 | 2 | 0 | 22/25 | 90% |
| plugin-skill-auditor | 0 | 0 | 0 | 1 | 24/25 | 99% |
| project-workflow | 0 | 1 | 2 | 0 | 22/25 | 90% |
| surveil | 0 | 1 | 2 | 1 | 21/25 | 89% |
| testing | 0 | 1 | 3 | 1 | 20/25 | 86% |
| ui-ux-pro-max | 0 | 0 | 3 | 2 | 20/25 | 90% |
| vercel-react-best-practices | 0 | 0 | 2 | 2 | 21/25 | 93% |
| vercel-react-native-skills | 0 | 0 | 2 | 1 | 22/25 | 94% |
| web-design-guidelines | 0 | 0 | 2 | 1 | 22/25 | 94% |
| windows-desktop | 0 | 0 | 0 | 0 | 25/25 | 100% |

## Stats

- **Skills audited:** 15
- **Average score:** 93%
- **Critical failures:** 0 (all skills have valid SKILL.md with proper frontmatter)
- **Perfect scores:** 1 (windows-desktop)
- **Most common issue:** M01 (no `allowed-tools` restriction) — 10 skills
- **Top recommendation:** Add `allowed-tools:` to frontmatter to restrict which tools the skill can use, preventing unintended side effects.

## Issue Frequency

| Rank | Check | Description | Count | Criticality |
|------|-------|-------------|-------|-------------|
| 1 | M01 | No `allowed-tools` restriction | 10 | Medium |
| 2 | M04 | Non-standard frontmatter fields | 8 | Medium |
| 3 | L04 | Missing "Common Mistakes" section | 7 | Low |
| 4 | H01 | Description lacks "use when" triggers | 5 | High |
| 5 | L02 | Description outside 20-300 char range | 4 | Low |
| 6 | M02 | Verbose body without references/ | 3 | Medium |
| 7 | L05 | Description keyword stuffing (>500 chars) | 2 | Low |
| 8 | H02 | SKILL.md over 500 lines | 1 | High |
| 9 | M05 | Deeply nested references | 1 | Medium |
| 10 | M08 | Multi-step skill missing `context: fork` | 1 | Medium |

## Scoring Methodology

Each check has a weight by criticality:
- **Critical:** 8 points each (4 checks = 32 points)
- **High:** 4 points each (6 checks = 24 points)
- **Medium:** 2 points each (10 checks = 20 points)
- **Low:** 1 point each (5 checks = 5 points)
- **Total possible: 81 points**
- **Score% = (earned points / 81) x 100**
