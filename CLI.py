import csv
import sys
import re

REQUIRED_KEYS = {
    "package_name",
    "repo_url",
    "repo_mode",
    "package_version",
    "filter_substring"
}

def read_config(file_path):
    try:
        with open(file_path, newline='') as f:
            # Построчно считываем CSV файл
            reader = csv.reader(f)
            config = {}
            for row in reader:
                if len(row) != 2:
                    print("Ошибка: неправильный формат строки")
                    sys.exit(1)
                key, value = row
                key = key.strip()
                value = value.strip()
                if key not in REQUIRED_KEYS:
                    print(f"Ошибка: неизвестный параметр {key}")
                    sys.exit(1)
                # Сохраняем параметр в словарь
                config[key] = value
            return config
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        sys.exit(1)

def validate(config):
    if not config["package_name"]:
        print("Ошибка в параметре: package_name")
        sys.exit(1)

    if not config["repo_url"] or not (re.match(r"^https?://", config["repo_url"])):
        print("Ошибка в параметре: repo_url")
        sys.exit(1)

    if config["repo_mode"] not in ("local", "remote"):
        print("Ошибка в параметре: repo_mode")
        sys.exit(1)

    if not config["package_version"] or not re.fullmatch(r"\d[\w.\-\+]*", config["package_version"]):
        print("Ошибка в параметре: package_version")
        sys.exit(1)

    if not config["filter_substring"]:
        print("Ошибка в параметре: filter_substring")
        sys.exit(1)

def main():
    # Проверяем, указан ли файл в аргументах командной строки
    if len(sys.argv) < 2:
        print("Ошибка: не указан файл")
        sys.exit(1)

    config = read_config(sys.argv[1])
    validate(config)

    for key, value in config.items():
        print(f"{key}: {value}")

main()

