# Readability Analyzer

This is a Python script that analyzes the readability of a given text file in **Russian**. It calculates the readability score based on the number of syllables, sentences, and words in the text.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your machine
- `nltk` library installed (`pip install nltk`)

## Usage

1. Copy the code into a Python file (e.g., `readability_analyzer.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script with the following command:

```
python readability_analyzer.py <path_to_text_file>
```

Replace `<path_to_text_file>` with the path to the text file you want to analyze.

5. You will be prompted to enter the number of the option you want to choose:

- Enter `1` to analyze the readability of the entire text.
- Enter `2` to analyze the readability of paragraphs in the text.
- Enter `3` to analyze the readability of chapters in the text.

6. The script will display the readability score for the selected option.

## Functions

The script contains the following functions:

- `syllable_count(text)`: Counts the number of syllables in the given text.
- `sentence_count(text)`: Counts the number of sentences in the given text.
- `words_count(text)`: Counts the number of words in the given text.
- `readability_score(syllables, sentences, words)`: Calculates the readability score based on the number of syllables, sentences, and words.
- `readability_of_text(whole_text)`: Analyzes the readability of the entire text.
- `readability_of_paragraph(text)`: Analyzes the readability of paragraphs in the text.
- `readability_of_chapter(text)`: Analyzes the readability of chapters in the text.
