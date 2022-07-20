import pandas as pd


def start():
    df = pd.read_csv('Data/Output/IPAVL_criterion_04_lemma_definition.csv')
    load_text()
    df_studies = load_text()
    df_sentences_final = pd.DataFrame(columns=['token_IPAVL', 'lemma_IPAVL', 'definition', 'Sentences', 'Study_ID'])
    for i, row in df.iterrows():
        print(i, row['token_IPAVL'])
        df_sentences = check_sentences(row['lemma_CPAVL'], df_studies)
        for i2, row2 in df_sentences.iterrows():
            df_sentences_final.loc[len(df_sentences_final)] = [row['token_IPAVL'], row['lemma_CPAVL'], row['definition'],
                                                               row2['Sentences'], row2['Study_ID']]
    df_sentences_final.to_csv(r'Data/Output/IPAVL_criterion_04_lemma_sentences.csv', index=False)
    print('-> A new file was generated: Data/Output/IPAVL_criterion_04_lemma_sentences.csv')


def check_sentences(term, df_studies):
    df_sentences = pd.DataFrame(columns=['Study_ID', 'Sentences'])
    for i, row in df_studies.iterrows():
        lst_sentences = check_sentence(term, row['Sentences'])
        for sentence in lst_sentences:
            df_sentences.loc[len(df_sentences)] = [row['Study_ID'], sentence]
    return df_sentences


def check_sentence(term, study):
    lst_paper_sentences = study.split('.')
    lst_sentences = []

    for paper_sentence in lst_paper_sentences:
        lst_words = paper_sentence.split(' ')
        i = 0
        for word in lst_words:
            if word is term:
                lst_sentences.append(format_sentence(i, lst_words))
                break
            i = i + 1

    return lst_sentences


def format_sentence(i, lst_words):
    start = i - 2
    end = i + 2
    if start < 0:
        start = 0

    if end > len(lst_words):
        end = i

    string = "[...] "
    try:
        while start < end:
            string = string + lst_words[start] + " "
            start = start + 1
    except:
        string = string + "there is a problem here"
        print(f'Erro: {lst_words}, {start}')

    string = string + " [...]"
    return string


def load_text():
    df_studies = pd.DataFrame(columns=['Study_ID', 'Sentences'])
    i = 1
    while i < 10:
        f = open(f'Data/Input/Corpus-new/S0{i}.txt', "r", encoding="utf8")
        df_studies.loc[i] = [f'S0{i}', f.read().replace('\n', ' ').lower()]
        i = i + 1

    while i < 26:
        f = open(f'Data/Input/Corpus-new/S{i}.txt', "r", encoding="utf8")
        df_studies.loc[i] = [f'S{i}', f.read().replace('\n', ' ').lower()]
        i = i + 1
    return df_studies
