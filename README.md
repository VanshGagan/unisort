# UniSort


**UniSort** is a lightweight command-line tool for interactively sorting files based on file types and user-defined destination folders.  
It is designed to help organize files in a configurable and modular way, keeping the code clean and easily extendable for future features.

---

## 📂 Project Structure
unisort/
│
├── main.py # Entry point of the program
├── sorter.py # Core logic for interactive file sorting
├── config.py # Handles loading of configuration from config.json
├── utils.py # Helper functions and ASCII art
├── config.json # User-defined configuration for source/destination folders and file types
└── README.md # Project documentation



---

## ⚙️ Configuration

The program uses a `config.json` file to define the source folder, destination folders, and file types to sort.  
This allows easy adjustments without modifying the code.

Example structure of `config.json`:

```json
{
  "source_folder": "~/Downloads",
  "destination_folders": {
    "Documents": "~/Documents",
    "Images": "~/Pictures",
    "Videos": "~/Videos"
  },
  "file_types": [".pdf", ".txt", ".jpg", ".png", ".mp4"]
}
```

source_folder → folder where files are located

destination_folders → target folders for sorting

file_types → only files with these extensions will be conside


### Features

Interactive CLI sorting using inquirer

Fully configurable via config.json

Clean, modular Python structure

Skips files that do not match the configured file types

Ready for extension with future features like automatic sorting, logging, or enhanced CLI interface


