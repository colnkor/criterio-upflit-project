import yaml

def load_config(config_path="config.yaml"):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            if config is None:
                raise Exception("Конфиг не загружен и равен None")
            return config
    except FileNotFoundError:
        print(f"Ошибка: Файл {config_path} не найден.")
        return {}
    except yaml.YAMLError as exc:
        print(f"Ошибка при парсинге YAML: {exc}")
        return {}

config = load_config()