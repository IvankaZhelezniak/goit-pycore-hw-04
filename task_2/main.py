import sys
import json
from processing import get_cats_info

def main():
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до файлу як аргумент.")
        sys.exit(1)

    file_path = sys.argv[1]
    cats_info = get_cats_info(file_path)
    print(json.dumps(cats_info, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
