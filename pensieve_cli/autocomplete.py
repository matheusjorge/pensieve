from .env import NOTES_PATH

def find_dirs(incomplete_path: str):
    subdirs = [
        str(f).replace(str(NOTES_PATH), "")[1:]
        for f in NOTES_PATH.glob(f"{incomplete_path}*/*")
    ]
    subdirs += [
        str(f).replace(str(NOTES_PATH), "")[1:]
        for f in NOTES_PATH.glob(f"{incomplete_path}*[!.md]")
    ]
    return subdirs

def find_files(incomplete_path: str):
    files = [
        str(f).replace(str(NOTES_PATH), "")[1:]
        for f in NOTES_PATH.glob(f"{incomplete_path}*.md")
    ]
    return files


def autocomplete(incomplete_path: str):
    return find_dirs(incomplete_path) + find_files(incomplete_path)
