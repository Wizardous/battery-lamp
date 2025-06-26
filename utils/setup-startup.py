import json
import os
from pathlib import Path

from win32com.client import Dispatch


# Path Constants.
WIN_USR_APPDATA= Path(os.environ["APPDATA"]).absolute()
PROJ_BASE_PATH = Path(__file__).parent.parent.absolute()
CONFIG_PATH    = PROJ_BASE_PATH / "setup_config.json"


# Load config
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)


# Find the pythonw.exe in the current virtual environment, require venv
if config.get("require_venv", True):
    venv_dir = Path(os.environ.get("VIRTUAL_ENV"))

    if not venv_dir:
        error_message = (
            "A Python virtual environment must be activated to run this script."
            "NOTE: To turn this requirement off set the option 'require_venv' to 'false' in the setup_config.json file."
        )
        raise EnvironmentError(error_message)
    
    pythonw = venv_dir / "Scripts" / "pythonw.exe"

    if not pythonw.exists():
        raise FileNotFoundError(f"pythonw.exe not found in the virtual environment at {pythonw}")
else:
    pythonw = "pythonw.exe"  # fallback


# Paths from config
script: Path = PROJ_BASE_PATH / config["script_path"]
icon: Path  = PROJ_BASE_PATH / config["icon_path"]
shortcut_name: str = config["shortcut_name"]

# Get the path to the user's Startup folder
startup: Path = WIN_USR_APPDATA / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
shortcut_path: Path = startup / shortcut_name

# Check if the shortcut_path already exists.
if shortcut_path.exists():
   print(f"WARNING: Startup shortcut already present at {shortcut_path}")
   print("Aborting.")
   exit(0) 


# Show details and confirm with user before proceeding
print("Shortcut will be created with the following details:")
print(f"  Shortcut path: {shortcut_path}")
print(f"  Target (pythonw): {pythonw}")
print(f"  Script: {script}")
print(f"  Icon: {icon}")
print(f"  Working Directory: {script.parent}")
print()

confirm = input("Proceed with creating the shortcut? [y/N]: ").strip().lower()
if confirm != "y":
    print("Aborted by user.")
    exit(0)

# Create a Shortcut link at Windows Startup folder.
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(str(shortcut_path.absolute()))
shortcut.Targetpath = str(pythonw)
shortcut.Arguments = f'"{script}"'
shortcut.WorkingDirectory = str(script.parent)
shortcut.IconLocation = str(icon)
shortcut.save()

print(f"Shortcut created at: {shortcut_path}")