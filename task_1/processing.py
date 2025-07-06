def total_salary(path: str) -> tuple[int, float]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                parts = line.strip().split(",")
                salaries.append(int(parts[-1]))
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0   # Обчислює середню зарплату лише якщо список не порожній
            return total, average
    except FileNotFoundError:
        print(f"❌ Файл '{path}' не знайдено.")
        return 0, 0
    except UnicodeDecodeError:
        print(f"❌ Помилка кодування. Файл '{path}' не в UTF-8.")
        return 0, 0
    except Exception as e:
        print(f"❌ Невідома помилка: {e}")
        return 0, 0
