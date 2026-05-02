param(
  [string]$Source = ".data\dongjun.db",
  [string]$DestinationDir = ".data\backups"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Source)) {
  throw "SQLite DB not found: $Source"
}

New-Item -ItemType Directory -Force -Path $DestinationDir | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$dest = Join-Path $DestinationDir "dongjun-$timestamp.db"

Copy-Item -LiteralPath $Source -Destination $dest -Force
Write-Output "Backup created: $dest"
