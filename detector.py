import pickle
import os
import re

PICKLE_PATH = os.path.join(os.path.dirname(__file__), "words_set.pkl")

with open(PICKLE_PATH, "rb") as file:
    words_set = pickle.load(file)


def words_check(text):
    """Analyzes the given text and returns a score (0 - 1) based on recognized words."""
    text = text.lower()

    # Remove punctuation except for letters, numbers, hyphens, and apostrophes
    split_text = [re.sub(r"[^\w'-]", "", word) for word in text.split()]

    # Filter out empty words after cleaning
    split_text = [word for word in split_text if word]

    if not split_text:
        return 0.0

    existing_words = sum(1 for word in split_text if word in words_set)

    return existing_words / len(split_text)
