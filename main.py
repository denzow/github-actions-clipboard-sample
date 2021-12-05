import argparse
from pyperclip import copy


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--text',
        help='text for clipboard',
        required=True,
    )
    args = parser.parse_args()
    return args.text


def main(text_for_clipboard: str):
    copy(text_for_clipboard)
    print(f'copied: {text_for_clipboard}')


if __name__ == '__main__':
    text_for_clipboard = init()
    main(text_for_clipboard)
