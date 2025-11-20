# PowerShell script to run Python file as module
param(
    [string]$FilePath
)

# Get the workspace root (parent of .vscode folder)
$workspaceRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Leaf
$currentDir = Split-Path $PSScriptRoot -Parent

# Get the file path relative to workspace root
$fullPath = Resolve-Path $FilePath
$relativePath = [System.IO.Path]::GetRelativePath($currentDir, $fullPath)

# Convert to module path (replace backslashes with dots, remove .py extension)
$modulePath = $relativePath -replace '\.py$', '' -replace '\\', '.' -replace '/', '.'

# Remove leading dots and clean up
$modulePath = $modulePath -replace '^\.+', ''

# Run as module
Write-Host "Running: python -m $modulePath" -ForegroundColor Cyan
python -m $modulePath
