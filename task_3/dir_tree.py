import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory_tree(path: Path, prefix=""):
    try:
        for item in sorted(path.iterdir()):              # Перебирає всі елементи в директорії path, відсортовані за іменем.
            if item.is_dir():                             # Перевіряє, чи є item папкою (директорією).
                print(f"{prefix}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
                # Рекурсивно викликає функцію для виведення вмісту піддиректорії, додаючи відступ.
                print_directory_tree(item, prefix + "    ")
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        # Обробляє помилку доступу, якщо немає прав на читання вмісту директорії.
        print(f"{prefix}{Fore.RED}[Немає доступу)]{Style.RESET_ALL} {path}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}❌ Будь ласка, вкажіть шлях до директорії як аргумент.{Style.RESET_ALL}")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}❌ Вказаний шлях не існує.{Style.RESET_ALL}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}❌ Вказаний шлях не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.MAGENTA}{dir_path.name}/{Style.RESET_ALL}")
    print_directory_tree(dir_path, "    ")

if __name__ == "__main__":
    main()


#   python dir_tree.py c:/projects/python_projects/goit-pycore-hw-04/task_2         запуск програми
