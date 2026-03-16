#  UniSort 📂

UniSort is a command-line tool designed to keep your workspace tidy. It makes sorting files effortless—no more tedious dragging and dropping files manually.

Just set your source folder, define your destination folders, and specify the file types you want to organize.
Run the program and quickly sort each file using a clean, interactive UI.

## ✨ Features
* **Interactive Setup:** Easily configure your source and destination folders.
* **Custom Rules:** Define which file types (e.g., .pdf, .png) go to which folder.
* **Interactive UI:** Moves files easialy with the interactive interface.
* **Reset Option:** Quickly clear your settings and start fresh.

## 🚀 How to Use

### 1. Installation
Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/VanshGagan/unisort.git](https://github.com/VanshGagan/unisort.git)
cd unisort
pip install -r requirements.txt
```
### 2. Configuration
Before sorting, run the setup wizard to define your folders and rules. This will update the config.json file in your project directory:

```bash
python3 main.py --setup
```

### 3. Running the sorter 
Once configured, simply run the script to organize your files. UniSort will read your config.json and move all matching files to their designated folders:

```bash
python3 main.py
```

### 4. Resetting 
To clear all saved configurations and delete the config.json file:


```bash
python3 main.py --clearsetup
```

## Arguments

Argument  | Function
------------------- | --------------------------------
--help or -h        | list of available arguments
--setup or -s       | Opens the configuration menu.
--clearsetup or -cs | Deletes the current config.json.



I am currently working on a solution to bundle the tool as a standalone executable, allowing you to call it directly from your command line as a global system command.

#  Created to keep your folders clean 🤙
