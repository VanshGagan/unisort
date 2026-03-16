import config
from sorter import run_sorter
from utils import ASCII_ART
from setup import run_setup
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s","--setup", help="Edit your source-folder, destination-folders or file types",
                        action="store_true")
    
    parser.add_argument("--cs","--clearsetup", help="clear your setup json file.",
                        action="store_true")
    
    args = parser.parse_args()
    if args.s:
        run_setup()
    elif args.cs:
        config.clear_config()

    else:
        cfg = config.load_config()
        run_sorter(cfg)


if __name__ == "__main__":
    print(ASCII_ART)
    main()