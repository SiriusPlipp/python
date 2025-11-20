#!/usr/bin/env python3
"""
Helper script to run a Python file as a module using python -m
Usage: python run_as_module.py <file_path>
"""
import sys
import os
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python run_as_module.py <file_path>")
    sys.exit(1)

file_path = Path(sys.argv[1]).resolve()
workspace_root = Path(__file__).parent.parent.resolve()

# Get relative path from workspace root
try:
    relative_path = file_path.relative_to(workspace_root)
except ValueError:
    print(f"Error: {file_path} is not within workspace root {workspace_root}")
    sys.exit(1)

# Convert to module path
module_path = str(relative_path).replace(os.sep, '.').replace('/', '.').replace('.py', '')
module_path = module_path.lstrip('.')

# Run as module (no extra output)
import subprocess
result = subprocess.run(["python", "-m", module_path], cwd=workspace_root)
sys.exit(result.returncode)

