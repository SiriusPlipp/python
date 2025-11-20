# Python Module Runner Configuration

This workspace is configured to run Python files as modules using `python -m`.

## Features

1. **Run Python File as Module** - Main task that converts file paths to module notation
2. **Keyboard Shortcuts**:
   - `Ctrl+F5` - Run current Python file as module
   - `Ctrl+Shift+F5` - Run Python file as module (alternative method)

## How to Use

### Method 1: Using Tasks (Recommended)
1. Open a Python file
2. Press `Ctrl+Shift+P` to open Command Palette
3. Type "Tasks: Run Task"
4. Select "Run Python File as Module"
5. Or use keyboard shortcut `Ctrl+F5`

### Method 2: Using Code Runner Extension (For Top-Left Button)
1. Install the "Code Runner" extension by Jun Han (if not already installed)
2. The "Run Code" button (▶) in the top-right will use `python -m` automatically
3. You can also use `Ctrl+Alt+N` to run the current file

### Method 3: Right-Click Menu
- Right-click on a Python file in the explorer
- Select "Run Task"
- Choose "Run Python File as Module"

### Method 4: Terminal Command
You can also run directly from terminal:
```bash
python -m playground.straightgay
```

## Files Created

- `.vscode/tasks.json` - Task definitions
- `.vscode/settings.json` - Workspace settings
- `.vscode/keybindings.json` - Keyboard shortcuts
- `.vscode/run_as_module.py` - Helper script for path conversion
- `.vscode/launch.json` - Debug configuration

## Note

The built-in "Run Python File" button at the top-left (Python extension) cannot be directly overridden. 
Use Code Runner extension (Method 2) or keyboard shortcuts (Method 1) instead.

