import argparse

def words_check(text):
    text = text.lower()

    dict_path = 'words.txt'
    with open(dict_path, 'r') as file:
        en_words = file.read()

    split_text = text.split()
    words_count = len(split_text)

    existing_words = 0

    for word in split_text:
        if word in en_words:
            existing_words += 1
    return existing_words / words_count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Gibberish Checker',
        description='Returns a value between 0-1 relative to the rate of existing x non-existing words in the English language.'
    )
    parser.add_argument(
        'text',
        type=str,
        help='Text to be checked for gibberish.'
    )

    args = parser.parse_args()

    result = words_check(args.text)
    print(f'Gibberish score: {result}')
