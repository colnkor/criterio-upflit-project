import yaml

def load_config(config_path="config.yaml"):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            return config if config else {}
    except FileNotFoundError:
        print(f"Ошибка: Файл {config_path} не найден.")
        return {}
    except yaml.YAMLError as exc:
        print(f"Ошибка при парсинге YAML: {exc}")
        return {}

# Загружаем конфигурацию
config = load_config()

seed = config.get('seed')

print(seed)
