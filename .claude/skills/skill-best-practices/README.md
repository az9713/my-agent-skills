# skill-best-practices

A read-only Claude Code skill that audits installed personal skills against a 25-check best practices checklist and outputs ranked findings to the terminal.

## What It Does

When invoked, this skill reads every personal skill in `~/.claude/skills/`, parses each skill's `SKILL.md` and directory structure, and evaluates them against 25 best-practice checks drawn from official Anthropic guidance. It produces a per-skill report grouped by severity, a summary table with weighted scores, and a single top recommendation.

**This skill is strictly read-only.** It never creates, modifies, or deletes any files. All output goes to the terminal.

## Usage

```
/skill-best-practices              # Audit all personal skills
/skill-best-practices windows-desktop   # Audit a single skill
```

## Capabilities

- Audits all personal skills in `~/.claude/skills/` (or a single named skill)
- Parses YAML frontmatter fields and validates them against the known schema
- Checks directory structure, file references, naming conventions, and line counts
- Applies heuristic checks for side-effect safety, progressive disclosure, and writing style
- Produces a per-skill breakdown grouped by criticality (Critical > High > Medium > Low)
- Calculates a weighted score percentage for each skill (0-100%)
- Generates a summary table across all audited skills
- Reports the most common issue and a top recommendation
- Skips itself during "all" audits to avoid feedback loops

## The 25 Checks

The checklist lives in [`references/checklist.md`](references/checklist.md). Each check has an ID, detection logic, and a fix recommendation.

### Critical (C01-C04) — Skill is broken

These prevent the skill from loading at all.

| ID | Check | What It Detects |
|----|-------|-----------------|
| C01 | SKILL.md exists | Missing main skill file |
| C02 | YAML frontmatter present | Missing `---` delimiters at top of file |
| C03 | `name` field present | No `name:` key in frontmatter |
| C04 | `description` field present | No `description:` key in frontmatter |

### High (H01-H06) — Skill works poorly

The skill loads but has significant quality or discoverability issues.

| ID | Check | What It Detects |
|----|-------|-----------------|
| H01 | Description has "when to use" triggers | Description lacks "Use when..." or trigger phrases; Claude can't discover the skill |
| H02 | SKILL.md under 500 lines | Main file too long; should use `references/` for heavy content |
| H03 | All supporting files referenced | Files exist in directory but aren't linked from SKILL.md (invisible to agent) |
| H04 | `name` format valid | Name doesn't match `^[a-z0-9-]{1,64}$` |
| H05 | Folder name matches `name` field | Mismatch between directory name and frontmatter `name:` |
| H06 | Folder uses kebab-case | Directory name isn't lowercase-hyphenated |

### Medium (M01-M10) — Could be improved

The skill works but has room for meaningful improvement.

| ID | Check | What It Detects |
|----|-------|-----------------|
| M01 | Has `allowed-tools` restriction | No tool restrictions; skill can use any tool |
| M02 | Verbose body without references | >300 lines with no `references/` directory |
| M03 | No extraneous docs | README.md, CHANGELOG.md, LICENSE found in skill directory |
| M04 | Standard frontmatter fields only | Unknown fields like `triggers:`, `license:`, `metadata:` |
| M05 | No deep nesting (>1 level) | Files nested like `references/sub/file.md` |
| M06 | Long reference files have TOC | Reference files >100 lines without a Table of Contents heading |
| M07 | Side-effect skill has `disable-model-invocation` | Heuristic: skill body has deploy/commit/push/delete actions but no safety flag |
| M08 | Multi-step skill has `context: fork` | Heuristic: skill has Step 1/2/3 patterns suggesting long-running task |
| M09 | `$ARGUMENTS` has matching `argument-hint` | Body uses `$ARGUMENTS` but frontmatter lacks `argument-hint:` |
| M10 | No duplicated content | SKILL.md and reference files share 3+ identical headings |

### Low (L01-L05) — Nice-to-have

Polish and style improvements.

| ID | Check | What It Detects |
|----|-------|-----------------|
| L01 | Imperative writing style | Instructions use passive voice instead of imperatives ("Run X" not "X should be run") |
| L02 | Description length 20-300 chars | Too short (lacks context) or too long (summary instead of triggers) |
| L03 | Background skill has `user-invocable: false` | Pure reference material that shouldn't be user-invoked |
| L04 | Has Common Mistakes section | Missing troubleshooting/pitfalls section |
| L05 | Description under 500 chars | Keyword stuffing in description field |

## Scoring

Each check has a weight by criticality:

| Criticality | Points per check | Count | Max points |
|-------------|-----------------|-------|------------|
| Critical | 8 | 4 | 32 |
| High | 4 | 6 | 24 |
| Medium | 2 | 10 | 20 |
| Low | 1 | 5 | 5 |
| **Total** | | **25** | **81** |

**Score% = (earned points / 81) x 100**, rounded to the nearest integer.

## Where the Best Practices Come From

The 25 checks are derived from two primary sources:

1. **Anthropic's official Claude Code skills documentation** ([code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)) — Defines the skill file format, supported frontmatter fields (`name`, `description`, `allowed-tools`, `argument-hint`, `context`, `user-invocable`, `disable-model-invocation`), directory structure conventions, and the progressive disclosure pattern of using `references/` for heavy content.

2. **Anthropic's skill-creator guide** (the `skill-creator` skill from the `anthropic-agent-skills` marketplace) — Provides detailed guidance on Claude Search Optimization (CSO), description writing (start with "Use when...", never summarize workflow), naming conventions (kebab-case, verb-first), token efficiency, and the distinction between skill types (technique, pattern, reference).

Additional checks (M07, M08, L01, L03) apply heuristic reasoning informed by patterns observed across hundreds of real-world skills.

## Output Format

The audit produces three sections:

1. **Per-skill detail** — Each skill gets a section with every check listed as PASS or FAIL, grouped by criticality. Failed checks include a fix recommendation.

2. **Summary table** — One row per skill showing fail counts by severity, pass count, and weighted score%.

3. **Stats** — Total skills audited, average score, most common issue with count, and top recommendation.

## File Structure

```
skill-best-practices/
├── SKILL.md                      # Main skill (124 lines)
└── references/
    └── checklist.md              # 25 checks with detection logic and fixes (177 lines)
```
