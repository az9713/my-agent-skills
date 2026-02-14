# plugin-skill-auditor

A read-only Claude Code skill that inventories all personal skills and installed plugins, creates a full backup, and generates a comprehensive report with exact removal and restoration instructions for every item.

## What It Does

When invoked, this skill scans your entire Claude Code extension ecosystem — personal skills, plugin marketplaces, plugin cache, and user settings — creates a timestamped backup of everything, and writes a detailed `AUDIT-REPORT.md` with per-item removal and restoration commands.

**This skill never deletes, removes, uninstalls, or modifies anything.** It only reads existing files and creates new backup/report files.

## Usage

```
/plugin-skill-auditor                    # Backup to claude-code-backup-YYYY-MM-DD/
/plugin-skill-auditor my-backup-name     # Backup to my-backup-name/
```

## Capabilities

### Inventory & Discovery

- **Personal skills** (`~/.claude/skills/`) — Reads each skill's `SKILL.md` frontmatter (name, description), lists all supporting files (excluding `node_modules`), and copies the entire directory to the backup
- **Plugin marketplaces** (`~/.claude/plugins/marketplaces/`) — Reads each `marketplace.json`, records the marketplace name, owner, description, git remote URL, and full list of available plugins
- **Plugin cache** (`~/.claude/plugins/cache/`) — Lists all cached plugin entries and their versions
- **Enabled plugins** (`~/.claude/settings.json`) — Reads the `enabledPlugins` object and records which plugins are active and which marketplace they come from

### Cross-Referencing

For each enabled plugin, the skill determines:
- Which marketplace it belongs to
- What skills, agents, and commands it provides (by parsing `marketplace.json` plugin entries)
- The original source (git URL or local path)

### Backup

Creates a timestamped directory in the current working directory:

```
claude-code-backup-YYYY-MM-DD/
├── skills/        # Full copies of all skill directories (follows symlinks)
├── plugins/       # Copies of all marketplace.json files
├── settings/      # Copy of settings.json
└── AUDIT-REPORT.md
```

- Uses `cp -rL` to follow symlinks so backups contain real files
- Skips `node_modules` directories to save space

### Report Generation

The `AUDIT-REPORT.md` contains these sections:

| Section | Content |
|---------|---------|
| **Overview Summary** | Total counts of skills, marketplaces, enabled plugins, available plugins |
| **Personal Skills Inventory** | Per-skill details with location, description, supporting files, and exact `rm -rf` / `cp -r` commands |
| **Plugin Marketplaces Inventory** | Per-marketplace details with owner, source repo, plugin table (name/description/enabled), and removal/reinstall commands |
| **Enabled Plugins Detail** | Per-plugin details with settings key, provided skills/agents/commands, and disable/re-enable JSON snippets |
| **Nuclear Option** | Single script to remove everything (skills + plugins + settings), with clear warnings |
| **Complete Restoration** | Step-by-step procedure to restore everything from the backup |

### Scope

| Scope | Audited? | Location |
|-------|----------|----------|
| Personal skills | Yes | `~/.claude/skills/` |
| Plugin marketplaces | Yes | `~/.claude/plugins/marketplaces/` |
| Plugin cache | Yes | `~/.claude/plugins/cache/` |
| User settings | Yes | `~/.claude/settings.json` |
| Project skills | No | `.claude/skills/` (per-project) |
| Enterprise skills | No | Managed settings (org-wide) |

## Safety Constraints

- **NEVER** deletes, removes, or uninstalls anything
- **NEVER** modifies `settings.json` or any plugin/skill files
- **ONLY** creates new files in the backup directory
- **ONLY** reads existing files for auditing
- Skips `node_modules` during copy and file listing
- Notes any unreadable files in the report and continues

## Allowed Tools

```
Bash(mkdir *), Bash(cp *), Bash(ls *), Bash(cat *), Bash(date *), Read, Grep, Glob, Write
```

## File Structure

```
plugin-skill-auditor/
└── SKILL.md    # Main skill (262 lines)
```
