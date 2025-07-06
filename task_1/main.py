import sys
from processing import total_salary

def main():
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до файлу як аргумент.")
        sys.exit(1)

    file_path = sys.argv[1]
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.2f}")

if __name__ == "__main__":
    main()
