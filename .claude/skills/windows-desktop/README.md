# windows-desktop

A Claude Code skill for controlling the Windows desktop via PowerShell. Provides commands for window management, application launching, system information, screenshots, audio control, clipboard operations, and more — with strict safety constraints that enforce read-only file access and prohibit destructive system operations.

## What It Does

When invoked, this skill gives Claude the ability to interact with the Windows desktop through PowerShell commands wrapped in `powershell.exe -Command "..."` syntax (for Bash tool compatibility). It covers 16 categories of desktop operations, with clear boundaries on what is and isn't allowed.

## Usage

This skill activates automatically when Claude detects Windows desktop operation requests:

```
"List my open windows"
"Take a screenshot"
"What's my CPU usage?"
"Set volume to 50%"
"Launch Notepad"
"Snap this window to the left half"
```

## Capabilities

### 16 Operation Categories

| # | Category | Read-Only? | What It Can Do |
|---|----------|-----------|----------------|
| 1 | **Window Management** | No | List visible windows, get active window, minimize/maximize/restore, move/resize, snap left/right, set always-on-top, close gracefully (WM_CLOSE), bring to foreground |
| 2 | **Application Management** | Mixed | List running processes (by CPU or memory), find specific processes, launch apps (including UWP/Store apps), switch to running apps |
| 3 | **Clipboard** | No | Read clipboard text, copy text to clipboard, check clipboard content type |
| 4 | **Display Info** | Read-only | Screen resolution, list all monitors, DPI scaling, display brightness |
| 5 | **Audio/Volume** | No | Get current volume level, set volume (0-100%), mute/unmute, list audio devices |
| 6 | **System Info** | Read-only | Full system summary (OS, CPU, RAM, uptime, battery), disk usage, CPU load snapshot, GPU info |
| 7 | **Network Info** | Read-only | IP addresses, WiFi status, network adapters, DNS servers, default gateway, public IP, connection test (ping) |
| 8 | **File/Directory** | **Strictly read-only** | List contents, search by name/content, get file properties/hash, directory size, read file content, count files by extension |
| 9 | **Virtual Desktops** | No | List desktops, create new (Win+Ctrl+D), switch next/previous |
| 10 | **Screenshot** | No | Full screen, active window, specific region, multi-monitor — saves to `%TEMP%` |
| 11 | **Power Management** | No | Lock screen, sleep, turn off monitor. **No shutdown or restart.** |
| 12 | **Notifications** | No | Send Windows toast notifications (WinRT or BurntToast) |
| 13 | **Services** | Read-only | List all/running services, get specific service status, search by name |
| 14 | **Installed Software** | Read-only | List installed programs (32-bit + 64-bit), search by name, list UWP/Store apps |
| 15 | **Environment Variables** | Read-only | List all variables, get specific, show PATH as list, system vs user variables |
| 16 | **Keyboard/Mouse** | No | Send keystrokes, special keys, keyboard shortcuts, move mouse, click (left/right/double), get mouse position |

### Safety Rules — Absolute Constraints

The skill enforces strict safety boundaries. These are non-negotiable:

**Prohibited commands (never executed):**

| Category | Blocked Commands |
|----------|-----------------|
| File write/delete | `Remove-Item`, `Delete`, `Move-Item`, `Rename-Item`, `Set-Content`, `Add-Content`, `Out-File`, `New-Item`, `Copy-Item`, `rm`, `del`, `ren`, `move`, `rd`, `rmdir`, `mkdir` |
| Process kill | `Stop-Process`, `Kill`, `taskkill` |
| Shutdown/restart | `Restart-Computer`, `Stop-Computer`, `shutdown`, `shutdown.exe` |
| Registry write | `Set-ItemProperty`, `New-ItemProperty`, `Remove-ItemProperty` on HKLM/HKCU |
| Service control | `Start-Service`, `Stop-Service`, `Set-Service`, `Restart-Service` |
| Network changes | `Set-NetAdapter`, `Disable-NetAdapter`, `Set-DnsClientServerAddress`, `netsh` (write ops) |
| User/security | `Set-LocalUser`, `New-LocalUser`, `Remove-LocalUser`, `icacls` (write), `takeown` |
| Execution policy | `Set-ExecutionPolicy` |
| Firewall | `Set-NetFirewallRule`, `New-NetFirewallRule`, `Remove-NetFirewallRule` |
| Scheduled tasks | `Register-ScheduledTask`, `Unregister-ScheduledTask` |

**Additional rules:**
- Never pipe output to files (`>`, `>>`, `Out-File`, `Set-Content`)
- Never use `Invoke-Expression` on untrusted input
- Never download or execute remote scripts
- Never modify environment variables persistently
- Screenshot is the only file-creation exception (saves to `%TEMP%`)

## Allowed Tools

```
Bash(powershell.exe *), Bash(powershell *), Bash(rundll32.exe *), Read, Glob, Grep
```

## File Structure

```
windows-desktop/
├── SKILL.md                  # Main skill with safety rules and quick reference (135 lines)
└── powershell-reference.md   # Full command reference for all 16 categories (569 lines)
```

The main `SKILL.md` contains the safety rules, operation category overview, quick reference examples, and common mistakes. The `powershell-reference.md` contains the complete command library with copy-paste-ready PowerShell snippets for every operation, plus `SendKeys` and virtual key code reference tables.
