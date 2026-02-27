import json
import config


def update_source():
    cfg = config.load_config()
    user_source = input("Please provide the path for your source-folder:   ")
    cfg["source_folder"] = user_source
    config.save_config(cfg)




def run_setup():
    print("--------// SETUP //--------")
    while True:
        ask_continue = input("Warning: Existing config will be overwritten.\n Continue? (y/n)   ")
        if ask_continue.lower() == "y":
            print("Proceeding with setup...")
            break
        elif ask_continue.lower() == "n":
            return
        else:
            print("Please write y or n")

    update_source()


