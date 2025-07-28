from pathlib import Path
from folder_manager import create_chapter_folders, create_subfolders

RESET = "\033[0m"
BOLD = "\033[1m"

# Colors
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"


def main():
    print(f"{BOLD}{MAGENTA}************* FOLDER CREATOR SETUP *************{RESET}")
    root = Path.cwd()
    episode_slug = input(f"{BOLD}{CYAN}Enter a slug/name for your episode folder (will be created inside current directory): {RESET}").strip()
    
    if not episode_slug:
        print(f"{BOLD}{RED}No slug entered, using current directory as root.{RESET}")
        base_path = root
    else:
        base_path = root / episode_slug
        base_path.mkdir(parents=True, exist_ok=True)
        print(f"{BOLD}{GREEN}Created/using episode folder: {base_path}{RESET}")

    num_chapters = int(input(f"{BOLD}{CYAN}How many chapters in your video? Please enter a number.{RESET}"))
    create_chapter_folders(base_path, num_chapters)

    while True:
        chapter_choice = input(f"{BOLD}{CYAN}Enter a chapter number to add subfolders to that chapter, or type 'done' to finish.{RESET}")
        if chapter_choice.lower() == 'done':
            break
        try:
            chapter_num = int(chapter_choice)
            chapter_path = base_path / f"chapter_{chapter_num}"
            if chapter_path.exists():
                create_subfolders(chapter_path)
            else:
                print(f"{BOLD}{RED}Chapter folder chapter_{chapter_num} does not exist.{RESET}")
        except ValueError:
            print(f"{BOLD}{CYAN}Please enter a valid chapter number.{RESET}")


    while True:
        print(f"{BOLD}{MAGENTA}\nOptions:{RESET}")
        print(f"{BOLD}{MAGENTA}1. Add subfolders{RESET}")
        print(f"{BOLD}{MAGENTA}2. Exit{RESET}")

        choice = input(f"{BOLD}{CYAN}Choose an option: {RESET}").strip()

        if choice == "1":
            chapter_choice = input(f"{BOLD}{CYAN}Enter chapter number: {RESET}").strip()
            chapter_path = base_path / f"chapter_{chapter_choice}"
            if chapter_path.exists():
                create_subfolders(chapter_path)
            else:
                print(f"{BOLD}{RED}That chapter folder doesn't exist.{RESET}")

        elif choice == "2":
            break
            

if __name__ == "__main__":
    main()