from config import load_config
from sorter import run_sorter
from utils import ASCII_ART


def main():
    config = load_config()
    run_sorter(config)


if __name__ == "__main__":
    print(ASCII_ART)
    main()