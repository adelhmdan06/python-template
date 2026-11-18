from pathlib import Path

def find_deep_files(folder_path):
    folder = Path(folder_path)

    return [
        file.name
        for file in folder.iterdir()
        if file.is_file() and file.name.startswith("deep")
    ]
