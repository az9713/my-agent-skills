#!/usr/bin/env bash
# mcp_doctor.sh - Diagnose broken MCP server configurations
# Works on Windows (Git Bash/MSYS2), macOS, and Linux
# Outputs JSON array of { name, status, reason, command } per server

set -euo pipefail

CONFIG_FILE="${HOME}/.claude/mcp.json"

if [[ ! -f "$CONFIG_FILE" ]]; then
   echo '{"error":"Config file not found","path":"'"$CONFIG_FILE"'"}'
   exit 1
fi

# Use node for JSON parsing and PATH-based binary lookup (no shell commands)
node -e '
const fs = require("fs");
const path = require("path");

function findInPath(cmd) {
   const dirs = (process.env.PATH || "").split(path.delimiter);
   const isWin = process.platform === "win32";
   const exts = isWin
      ? (process.env.PATHEXT || ".COM;.EXE;.BAT;.CMD;.JS").toLowerCase().split(";")
      : [""];

   for (const dir of dirs) {
      // Check with each extension
      for (const ext of exts) {
         const full = path.join(dir, cmd + ext);
         try { fs.accessSync(full, fs.constants.X_OK); return full; } catch {}
      }
      // Check bare name (handles cases like "npx" on unix)
      if (!isWin) {
         const full = path.join(dir, cmd);
         try { fs.accessSync(full, fs.constants.X_OK); return full; } catch {}
      }
   }
   return null;
}

function checkBinary(bin) {
   if (path.isAbsolute(bin)) {
      return fs.existsSync(bin) ? { ok: true, path: bin } : { ok: false };
   }
   const found = findInPath(bin);
   return found ? { ok: true, path: found } : { ok: false };
}

function checkDocker() {
   try {
      require("child_process").execSync("docker info", {
         stdio: "pipe",
         timeout: 5000
      });
      return true;
   } catch {
      return false;
   }
}

// Read and parse config
let config;
try {
   config = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
} catch (e) {
   console.log(JSON.stringify({ error: "Failed to parse config", detail: e.message }));
   process.exit(1);
}

const servers = config.mcpServers || {};
const results = [];

for (const [name, entry] of Object.entries(servers)) {
   // Skip disabled servers
   if (entry.disabled === true) {
      results.push({ name, status: "SKIP", reason: "Already disabled", command: entry.command || "" });
      continue;
   }

   const command = entry.command || "";
   const args = entry.args || [];
   let status = "OK";
   let reason = "";
   const warnings = [];

   // Resolve actual binary (Windows cmd /c <real-binary> pattern)
   let binaryToCheck = command;
   let argsStartIdx = 0;

   if (command === "cmd" && args.length >= 2 && args[0] === "/c") {
      binaryToCheck = args[1];
      argsStartIdx = 2;
   }

   // Check binary exists
   const binResult = checkBinary(binaryToCheck);
   if (!binResult.ok) {
      status = "FAIL";
      reason = path.isAbsolute(binaryToCheck)
         ? "Binary not found: " + binaryToCheck
         : "Command not found in PATH: " + binaryToCheck;
   }

   // Docker-specific: check daemon is running
   if (status === "OK" && binaryToCheck === "docker") {
      if (!checkDocker()) {
         status = "FAIL";
         reason = "Docker daemon not running or not accessible";
      }
   }

   // Check absolute paths in args (skip flags and URLs)
   if (status === "OK") {
      for (let i = argsStartIdx; i < args.length; i++) {
         const arg = args[i];
         if (typeof arg !== "string") continue;
         if (arg.startsWith("-") || arg.startsWith("http")) continue;
         if (path.isAbsolute(arg) && !fs.existsSync(arg)) {
            warnings.push("Arg path not found: " + arg);
         }
      }
      if (warnings.length > 0) {
         status = "WARN";
         reason = warnings.join("; ");
      }
   }

   results.push({ name, status, reason, command: binaryToCheck });
}

console.log(JSON.stringify(results, null, 2));
' "$CONFIG_FILE"
