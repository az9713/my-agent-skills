---
name: windows-diagnostics
description: "360-degree Windows system health diagnostics — covers CPU, memory, disk, network, security, startup programs, services, system info, hardware, and installed software. Use this skill whenever the user mentions system diagnostics, PC health check, performance issues, 'why is my computer slow', disk space, memory usage, startup optimization, security audit, bloatware removal, system cleanup, laptop health, or wants to keep their PC in prime condition. Also use when the user asks about high CPU, RAM usage, what's eating their disk, or wants a full system report."
---

# Windows 360° System Diagnostics

Performs a comprehensive system health check across 10 categories, generates a severity-classified HTML report, and summarizes findings with actionable recommendations.

## How to Run

### Step 1: Collect diagnostics data

Run the PowerShell collection script. It gathers data across all 10 diagnostic categories and outputs JSON:

```bash
powershell -NoProfile -ExecutionPolicy Bypass -File "C:/Users/simon/.claude/skills/windows-diagnostics/scripts/collect_diagnostics.ps1"
```

The script outputs JSON to stdout and saves it to `%TEMP%\windows_diagnostics.json`. Each section has its own error handling — if one category fails (e.g., Defender status requires admin), the rest still complete.

### Step 2: Generate the HTML report

```bash
python "C:/Users/simon/.claude/skills/windows-diagnostics/scripts/generate_report.py"
```

This reads the JSON, applies severity rules, and produces a styled HTML report at `./SystemHealthReport_YYYY-MM-DD.html` (in the current working directory). It also prints a summary to stdout.

Optionally specify a custom output path:
```bash
python "C:/Users/simon/.claude/skills/windows-diagnostics/scripts/generate_report.py" "/path/to/report.html"
```

### Step 3: Summarize to the user

After both scripts run, present findings to the user organized by severity:

1. **CRITICAL items first** — these need immediate attention
2. **WARNING items** — should be addressed soon
3. **INFO items** — optimization opportunities
4. **OK items** — briefly mention what's healthy (don't list every OK finding)

For each finding, include the recommendation. Be specific and actionable.

### Step 4: Offer follow-up actions

Based on findings, offer to help with:
- Removing bloatware (`Get-AppxPackage -Name "..." | Remove-AppxPackage`)
- Disabling unnecessary startup programs
- Running Disk Cleanup
- Investigating top resource consumers
- Checking specific error events in detail
- Re-running with admin privileges if security data was unavailable

## Admin vs Non-Admin

The script works without admin, but these features require elevation:
- Windows Defender detailed status
- Full event log access
- Physical disk SMART data
- Windows Update pending list (COM object)
- Secure Boot status

If key sections show errors, tell the user: "Some security checks require administrator privileges. Would you like me to explain how to re-run elevated?"

To re-run elevated, the user should open an admin terminal and run the same commands.

## Interpreting Results

Read `references/severity_rules.md` for the full classification rules. Key thresholds:
- Disk: <5% free = CRITICAL, <15% = WARNING
- Memory: >95% = CRITICAL, >85% = WARNING
- CPU: >95% = CRITICAL, >90% = WARNING
- Startup: >25 items = CRITICAL, >15 = WARNING
- Uptime: >60 days = CRITICAL, >30 = WARNING
- Any disabled security feature (Defender, Firewall) = CRITICAL

## Bloatware Reference

Read `references/known_bloatware.md` for the list of common pre-installed packages that can be safely removed, and which packages must NOT be removed.

## Important Notes

- The large file scan only covers Desktop, Documents, Downloads, and Videos to avoid long runtimes. It skips `node_modules`, `.git`, and `.venv` directories.
- Temperature data via WMI is unreliable on many consumer laptops. Don't alarm the user if thermal data is unavailable.
- The `Win32_Product` class is intentionally NOT used (it triggers MSI reconfiguration and is extremely slow). Software is enumerated from the registry instead.
- The health score is indicative, not absolute. A score of 100 means no issues were detected, not that the system is perfect.
