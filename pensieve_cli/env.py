import os
import pathlib

ROOT = os.getenv("PENSIEVE_ROOT", "./")
ROOT_PATH = pathlib.Path(ROOT)
NOTES_PATH = ROOT_PATH / "notes"
EDITOR = os.getenv("PENSIEVE_EDITOR", "nano")
