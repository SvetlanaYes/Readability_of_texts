import re
import sys
import nltk
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
#natasha , text without punctuation

mystem = Mystem()
russian_stopwords = stopwords.words("russian")


def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]

    text = " ".join(tokens)

    return text

def syllable_count(text):
    pattern = r"[ауоыиэяюёе]"
    result = re.findall(pattern, text.lower())
    return len(result)


def sentence_count(letter):
    #sentence tokenizer
    if letter in ['.', '!', '?']:
        return 1
    return 0


def words_count(text):
    #aranc punktuaciayi texty pahel
    tmp = text.split()
    count = len(tmp)
    if "-" in tmp:
        count -= 1
    return count


def readability_value(syllables, sentences, words):
    #score
    if sentences and words:
        return 208.75 - 1.08 * (syllables / sentences) - 65.14 * (syllables / words)
    return 0


def readability_of_text(whole_text):
    sentences = 0
    words = words_count(whole_text)
    syllables = syllable_count(whole_text)
    #tokenizer
    sentences = sentence_count(whole_text)
    print(readability_value(syllables, sentences, words))


def readability_of_paragraph(text):
    spl_text = text.split("\n")
    for paragraph in spl_text:
        syllables = syllable_count(paragraph)
        words = words_count(paragraph)
        sentences = sentence_count(paragraph)
        print(readability_value(syllables, sentences, words))


def readability_of_chapter(text):
    splted_text = text.split()
    chapter = set()
    size = len(splted_text)
    pattern = r"Глава\s*(.+)"
    result = re.search(pattern, text, 37)
    print(result)
    for i in range(0, size):
        if splted_text[i] == 'ГЛАВА' or splted_text[i] == 'Глава':
            i += 1
            sentences = 0
            count_of_words = 0
            count_of_syllables = 0
            while i < size and (splted_text[i] != 'ГЛАВА' and splted_text[i] != 'Глава'):
                for letter in splted_text[i]:
                    sentences += sentence_count(letter)
                count_of_words += 1
                count_of_syllables += syllable_count(splted_text[i])
                chapter.add(splted_text[i])
                i += 1
            print(readability_value(count_of_syllables, sentences, count_of_words))
        chapter.clear()


def main():
    try:
        arg = sys.argv[1]
    except IndexError:
        print("Please, write path name!")
        return

    print("Enter the number of option you want to choose : Readability of 1 - text, 2 - paragraphs, 3 - chapters")
    option = int(input())
    if option not in [1, 2, 3]:
        print("Enter correct value")
        return
    with open(arg, 'r', encoding='utf-8') as file:
        text = file.read()
        if option == 1:
            readability_of_text(text)
        elif option == 2:
            readability_of_paragraph(text)


if __name__ == "__main__":
    main()

