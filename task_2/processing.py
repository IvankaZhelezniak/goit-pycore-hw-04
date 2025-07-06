def get_cats_info(path: str) -> list[dict]:
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            cat_info = {}
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cat_dict = {
                        "id": cat_id.strip(),
                        "name": name.strip(),
                        "age": age.strip()
                    }
                    cats.append(cat_dict)
            return cats
    except FileNotFoundError:
        print(f"❌ Файл '{path}' не знайдено.")
        return []
    except UnicodeDecodeError:
        print(f"❌ Помилка кодування. Файл '{path}' не в UTF-8.")
        return []
    except Exception as e:
        print(f"❌ Невідома помилка: {e}")
        return []
    