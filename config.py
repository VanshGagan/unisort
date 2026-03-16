import json

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def save_config(config_file):
    with open("config.json", "w") as f:
        json.dump(config_file, f, indent=4)

def clear_config():
    empty_config = {
        "source_folder": "",
        "destination_folders": {}
    }
    save_config(empty_config)
    print("Configuration cleared and reset to defaults.")
