import os
from pathlib import Path 
import json

CONFIG_FILE = "config.json"

def create_chapter_folders(base_path: Path, num_chapters: int):
    chapter_printout = ""
    for i in range(1, num_chapters + 1):
        chapter_folder = base_path / f"chapter_{i}"
        chapter_folder.mkdir(parents=True, exist_ok=True)
        chapter_printout += f"{i}| "
        
    print(f"{BOLD}{GREEN}Created folders for chapters {chapter_printout}{RESET}")

def create_subfolders(chapter_path: Path):
    print(f"{BOLD}{GREEN}Adding subfolders to: {chapter_path}{RESET}")
    subfolder_printout = ""
    while True:
        subfolder_name = input(f"{BOLD}{CYAN}Enter subfolder name ***USE UNDERSCORES FOR SPACES***, or type 'done' to finish{RESET}").strip()
        if subfolder_name.lower() == 'done':
            break
        if subfolder_name == '':
            print(f"{BOLD}{RED}Folder name cannot be empty{RESET}")
            continue
        full_path = chapter_path / subfolder_name
        full_path.mkdir(parents=True, exist_ok=True)
        subfolder_printout += f"{subfolder_name}| "

    print(f"{BOLD}{GREEN}Created these subfolders: {subfolder_printout}{RESET}")
