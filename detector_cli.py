import argparse
import os
from detector import words_check


def analyze_text(text):
    """Analyze a given text and print the score of real words."""
    score = words_check(text)
    print(f"Real Words Score: {score:.2f}")


def analyze_file(file_path):
    """Read text from a file and analyze it."""
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().strip()

    if not text:
        print("Error: The file is empty.")
        return

    analyze_text(text)


def main():
    parser = argparse.ArgumentParser(description="Check percentage of real words or gibberish in a text.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--text", type=str, help="The text to analyze.")
    group.add_argument("-f", "--file", type=str, help="Path to a .txt file to analyze.")

    args = parser.parse_args()

    if args.text:
        analyze_text(args.text)
    elif args.file:
        analyze_file(args.file)


if __name__ == "__main__":
    main()
