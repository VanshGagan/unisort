#!/usr/bin/env python3

import os
import shutil
import json


ascii_art = """

  __  ___  ______________  ___  ______
 / / / / |/ /  _/ __/ __ \/ _ \/_  __/
/ /_/ /    // /_\ \/ /_/ / , _/ / /   
\____/_/|_/___/___/\____/_/|_| /_/    
                                      

"""


def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

source_folder = os.path.expanduser(load_config()['source_folder'])
destination_folders = {k: os.path.expanduser(v) for k, v in load_config()['destination_folders'].items()}

options = ", ".join(destination_folders.keys())

if __name__ == "__main__":
    print(ascii_art)
    for filename in os.listdir(source_folder):
        if filename.endswith('.pdf'):
            user_input = input(f"Move: {filename} to?\n{options}\n\n")
            for option, path in destination_folders.items():
                if user_input == option:
                    shutil.move(f"{source_folder}/{filename}", f"{path}")
                    print(f"Moved: {filename} to {option}")


            #https://python-inquirer.readthedocs.io/en/latest/usage.html

'''

for filename in os.listdir(downloads):
    if filename.endswith('.pdf'):
        user_input = input("Move: " + filename + " to? \n \n I for Info2 \n M for Mathe2 \n F for FoC \n B for BWL2 \n S for Statistik \n X to skip...   \n")
        if user_input.upper() == "I":
            shutil.move(downloads + '/' + filename, target + '/Info2/' + filename)#
            print("Moved: " + filename + " to Info2 \n \n ")
        elif user_input.upper() == "M":
            shutil.move(downloads + '/' + filename, target + '/Mathe2/' + filename)
            print("Moved: " + filename + " to Mathe2 \n \n ")
        elif user_input.upper() == "F":
            shutil.move(downloads + '/' + filename, target + '/FoC/' + filename)
            print("Moved: " + filename + " to FoC \n \n ")
        elif user_input.upper() == "B":
            shutil.move(downloads + '/' + filename, target + '/BWL2/' + filename)
            print("Moved: " + filename + " to BWL2 \n \n ")
        elif user_input.upper() == "S":
            shutil.move(downloads + '/' + filename, target + '/Statistik/' + filename)
            print("Moved: " + filename + " to Statistik \n \n ")
        elif user_input.upper() == "X":
            print("Skipped: " + filename + "\n \n ")
        else:
            print("Invalid input. Skipped: " + filename + "\n \n ")

    else:
        print("Skipped: " + filename + " (not a PDF) \n \n ")
print(" \n Nothing to sort // Exiting... \n \n ")

'''