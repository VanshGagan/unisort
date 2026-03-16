import os
import shutil
import inquirer
import time


def getAnswer(fname, destination_options):
    questions = [
    inquirer.List('folder',
                    message=f"Where do you want to move {fname}?",
                    choices=[option for option in destination_options.keys()],
                ),
    ]
    return inquirer.prompt(questions)["folder"]


def run_sorter(config):
    source_folder = os.path.expanduser(config['source_folder'])
    destination_folders = {k: os.path.expanduser(v) for k, v in config['destination_folders'].items()}


    for filename in os.listdir(source_folder):
        moved = False
        for ending in config["file_types"]:
            if filename.endswith(ending):
                awnser = getAnswer(filename, destination_folders)
                if awnser == "X":
                    print(f"Skipped: {filename} (skip selected by user) \n \n ")
                    time.sleep(1)
                    moved = True
                    continue
                for option, path in destination_folders.items():
                    if awnser == option:
                        shutil.move(f"{source_folder}/{filename}", f"{path}")
                        print(f"Moved: {filename} to {option}")
                        time.sleep(1)
                        moved = True

            elif moved == False:
                print(f"Skipped: {filename} (not a selected type) \n \n ")
                time.sleep(1)
    time.sleep(1)
    print(" \n Nothing to sort // Exiting... \n \n ")