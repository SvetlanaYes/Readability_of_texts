import re
import sys
import nltk


def syllable_count(text):
    pattern = r"[ауоыиэяюёе]"
    result = re.findall(pattern, text.lower())
    return len(result)


def sentence_count(text):
    return len(nltk.sent_tokenize(text, language="russian"))


def words_count(text):
    tmp = text.split()
    count = len(tmp)
    if "-" in tmp:
        count -= 1
    return count


def readability_score(syllables, sentences, words):
    if sentences and words:
        return 208.75 - 1.08 * (syllables / sentences) - 65.14 * (syllables / words)
    return 0


def readability_of_text(whole_text):
    sentences = 0
    words = words_count(whole_text)
    syllables = syllable_count(whole_text)
    sentences = sentence_count(whole_text)
    print(readability_score(syllables, sentences, words))


def readability_of_paragraph(text):
    spl_text = text.split("\n")
    for paragraph in spl_text:
        syllables = syllable_count(paragraph)
        words = words_count(paragraph)
        sentences = sentence_count(paragraph)
        print(readability_score(syllables, sentences, words))


def readability_of_chapter(text):
    splted_text = text.split()
    chapter = set()
    size = len(splted_text)
    pattern = r"Глава\s*(.+)"
    result = [(m.start(0), m.end(0)) for m in re.finditer(pattern, text)]
    for i in range(0,len(result)):
        if ( i == len(result) - 1 ):
            text_of_chapter = text[result[i][1]:]
        else:
            text_of_chapter = text[result[i][1]:result[i+1][0]]
        readability_of_text(text_of_chapter)
  


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
        elif option == 3:
            readability_of_chapter(text)

if __name__ == "__main__":
    main()

