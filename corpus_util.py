# Esta classe transforma o corpus.txt no formato .csv, com a frequência, o formato stemmer e o formato lemman
import pandas as pd


def corpus_to_lst():
    terms = []
    with open('Data/Output/corpus.txt', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            term = line.replace("\n", "") # limpando a quebra de linha e transformando em stemmer
            terms.append(term)
    return terms


def counter_terms(terms):
    df = pd.DataFrame(columns=['term', 'frequency'])

    from collections import Counter
    counter = Counter(terms)
    dictionary_terms = dict(counter)
    for dictionary_term in dictionary_terms.items():
        df.loc[len(df)] = [dictionary_term[0], dictionary_term[1]]

    return df


def convert_corpus(df_terms):
    df = pd.DataFrame(columns=['term', 'frequency', 'stemmer', 'lemma'])
    for i, row in df_terms.iterrows():
        term = row['term']
        df.loc[i] = [term, row['frequency'], stemmer(term), lemma(term)]
    return df


def stemmer(term):
    from nltk.stem import PorterStemmer
    porter = PorterStemmer()
    return porter.stem(term)


def lemma(term):
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(term)


def start():
    print('> Corpus_util Started <')

    lst_terms = corpus_to_lst()
    df_terms = counter_terms(lst_terms)
    df = convert_corpus(df_terms)

    df.to_csv(r'Data/Output/IPAVL.csv', index=False)
    print('-> A new file was generated: Data/Output/IPAVL.csv')
    print('--Corpus_util Finished--')