import json

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def save_config(config_file):
    with open("config.json", "w") as f:
        json.dump(config_file, f, indent=4)