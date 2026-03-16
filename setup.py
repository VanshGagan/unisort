import json
import time
import os
import config

def update_file_types():
    cfg = config.load_config()
    while True:

        file_type = input("Please provide the file types:  (x to end)   ").strip()
        if file_type.lower() == "x":
            break
        cfg["file_types"].append(file_type)
        config.save_config(cfg)

def update_destination():
    cfg = config.load_config()
    while True:

        destination_folder = input("Please provide the path for a destination-folder: (x to end)   ").strip()
        if destination_folder.lower() == "x":
            break
        user_destination = os.path.expanduser(destination_folder)
        if os.path.exists(user_destination):
            print("Proceeding...")
            time.sleep(1)
            folder_name = input("Please provide a name for the folder {user_destination}:  ")
            cfg["destination_folders"][folder_name] = user_destination
            config.save_config(cfg)

        else:
            print("please enter a valid path")

    update_file_types()

def update_source():
    cfg = config.load_config()
    while True:

        user_source = input("Please provide the path for your source-folder: (x to skip)   ").strip()
        user_source = os.path.expanduser(user_source)
        if os.path.exists(user_source):
            print("Proceeding...")
            time.sleep(1)
            break
        elif user_source.lower() == "x":
            break
        else:
            print("please enter a valid path")
    cfg["source_folder"] = user_source
    config.save_config(cfg)
    update_destination()






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


