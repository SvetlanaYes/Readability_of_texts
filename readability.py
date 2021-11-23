import re


def syllable_count(word_in_sentence):
    count = 0
    syllables = set("ауоыиэяюёе")
    pattern = r"[ауоыиэяюёе]"
    for letter in word_in_sentence:
        result = re.findall(pattern, word_in_sentence.lower())
        count += len(result)
    return count


def sentence_count(letter):
    if letter in ['.', '!', '?']:
        return 1
    return 0


def words_count(text):
    tmp = text.split()
    count = len(tmp)
    if "-" in tmp:
        count -= 1
    return count


def readability_value(syllables, sentences, words):
    if sentences:
        return 208.75 - 1.08 * (syllables / sentences) - 65.14 * (syllables / words)
    return 0


def readability(text):
    sentences = 0
    count_of_words = words_count(text)
    count_of_syllables = 0
    for letter in text:
        count_of_syllables += syllable_count(letter)
        sentences += sentence_count(letter)
    if sentences == 0 or count_of_words == 0:
        return 0
    return readability_value(count_of_syllables, sentences, count_of_words)


def readability_of_text(whole_text):
    tmp = whole_text.split()
    sentences = 0
    words = words_count(whole_text)
    syllables = 0
    for word in tmp:
        syllables += syllable_count(word)
        for letter in word:
            sentences += sentence_count(letter)
    print(syllables)
    print(readability_value(syllables, sentences, words))


def readability_of_paragraph(text_, paragraph_number):
    spl_text = text_.split("\n")
    text_without_empty_paragraphs = [None] * len(spl_text)
    j = 0
    for i in spl_text:
        if i == '':
            continue
        text_without_empty_paragraphs[j] = i
        j += 1
    if paragraph_number > j or paragraph_number < 1:
        return 0
    sentence = text_without_empty_paragraphs[paragraph_number - 1]
    print(readability(sentence))


def readability_of_chapter(text__, chapter_number):
    splted_text = text__.split()
    chapter = set()
    size = len(splted_text)
    pattern = r"Глава\s*(.+)"
    result = re.findall(pattern, text__)
    print(result)
    a = False
    for element in result:
        if element == chapter_number:
            a = True
    if not a:
        return 0
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
    with open("text.txt", 'r', encoding='utf-8') as file:
        tmp = file.read()
        readability_of_text(tmp)
        readability_of_paragraph(tmp, 2)
        readability_of_chapter(tmp, 1)


if __name__ == "__main__":
    main()

