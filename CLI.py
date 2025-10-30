import csv
import sys

REQUIRED_KEYS = {
    "package_name",
    "repo_url_or_path",
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
                    print("Ошибка в параметре: неправильный формат строки")
                    sys.exit(1)
                key, value = row
                # Сохраняем параметр в словарь
                config[key.strip()] = value.strip()
            return config
    except:
        print("Ошибка: файл не открывается")
        sys.exit(1)

def validate(config):
    if not config["package_name"]:
        print("Ошибка в параметре: package_name")
        sys.exit(1)

    if not config["repo_url_or_path"]:
        print("Ошибка в параметре: repo_url_or_path")
        sys.exit(1)

    if config["repo_mode"] not in ("local", "remote"):
        print("Ошибка в параметре: repo_mode")
        sys.exit(1)

    if not config["package_version"]:
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
