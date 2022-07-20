# Esta classe lê todos os arquivos e transforma em um corpus .txt com os termos.
def load_text():
    text = ""
    f = open("Data/Input/Corpus-new/S01.txt", "r", encoding="utf8")
    text = f.read()
    f = open("Data/Input/Corpus-new/S02.txt", "r", encoding="utf8")
    text = text + f.read()
    print(len(text))
    f = open("Data/Input/Corpus-new/S03.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S04.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S05.txt", "r", encoding="utf8")
    text = text + f.read()
    print(len(text))
    f = open("Data/Input/Corpus-new/S06.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S07.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S08.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S09.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S10.txt", "r", encoding="utf8")
    text = text + f.read()
    print(len(text))
    f = open("Data/Input/Corpus-new/S11.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S12.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S13.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S14.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S15.txt", "r", encoding="utf8")
    text = text + f.read()
    print(len(text))
    f = open("Data/Input/Corpus-new/S16.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S17.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S18.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S19.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S20.txt", "r", encoding="utf8")
    text = text + f.read()
    print(len(text))
    f = open("Data/Input/Corpus-new/S21.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S22.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S23.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S24.txt", "r", encoding="utf8")
    text = text + f.read()
    f = open("Data/Input/Corpus-new/S25.txt", "r", encoding="utf8")
    text = text + f.read()
    return text


def clean_text(text):
    # split into words
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text.lower())
    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]
    return words


def write_corpus(words):
    file = open("Data/Output/corpus.txt", "w", encoding="utf-8")
    for word in words:
        file.write(word + "\n")
    file.close()
    print('-> A new file was generated: Data/Output/corpus.txt')


def start():
    print('--Corpus Started--')
    text = load_text()
    words = clean_text(text)
    write_corpus(words)
    print('--Corpus Finished--')