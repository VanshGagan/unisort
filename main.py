from config import load_config
from sorter import run_sorter
from utils import ASCII_ART
from setup import run_setup
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--setup", help="choose your source-folder and the destination.",
                        action="store_true")
    args = parser.parse_args()
    if args.setup:
        run_setup()
    else:
        config = load_config()
        run_sorter(config)


if __name__ == "__main__":
    print(ASCII_ART)
    main()