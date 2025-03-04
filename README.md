# Gibberish Detector

## Overview

The **Gibberish Detector** is a simple Python script that evaluates whether a given text consists of meaningful words. It does this by comparing words in the input text against a predefined set of known words stored in `words_set.pkl`.

## How It Works

- The script loads a set of known words from `words_set.pkl`, which is included in this repository.
- It defines a function, `words_check(text)`, that:
  - Converts the input text to lowercase.
  - Splits the text into individual words.
  - Checks how many words exist in the known words set.
  - Returns a score between `0` and `1`, representing the proportion of recognized words.

## Installation

1. Clone this repository:
`git clone https://github.com/LMArantes/gibberish-detector.git cd gibberish-detector`
2. Ensure you have Python 3 installed.

## Usage

1. Import and use the `words_check` function:

```python
from gibberish_detector import words_check

text = "Hello world"
score = words_check(text)
print(f"Score: {score}")
```

## Score Interpretation

- 1.0 → All words are recognized.
- 0.0 → No words are recognized (likely gibberish).
- A score between 0.0 and 1.0 indicates partial recognition.

## License

This project is licensed under the **Modified Attribution License (MAL) v1.0**.  
See the [LICENSE](https://lmarantes.github.io/Modified-Attribution-License/) for details.