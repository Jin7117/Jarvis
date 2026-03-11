# file: open_paths.py
import os
from pathlib import Path

# Dictionary of common paths you might want
COMMON_PATHS = {
    "desktop": Path.home() / "Desktop",
    "documents": Path.home() / "Documents",
    "downloads": Path.home() / "Downloads",
}

def open_path(name_or_path):
   
    # Check if it's a known common path
    path = COMMON_PATHS.get(name_or_path.lower(), name_or_path)

    try:
        os.startfile(path)
        print(f"Opening: {path}")
    except FileNotFoundError:
        print(f"Path not found: {path}")
    except Exception as e:
        print(f"Error opening {path}: {e}")

# Example usage
if __name__ == "__main__":
    open_path("desktop")  # Opens Desktop
    open_path("c_drive")  # Opens C Drive
    open_path(r"C:\Users\YourUsername\Documents\example.txt")  # Opens a specific file