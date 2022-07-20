# Esta classe aplica o critério 01: remover as palavras mais populares com base na lista da GSL
import pandas as pd
import corpus_util as corpus_util


def convert_GSL(df_gsl):
    df = pd.DataFrame(columns=['term', 'stemmer', 'lemma'])
    for i, row in df_gsl.iterrows():
        term = row['Lemma']
        df.loc[i] = [term, corpus_util.stemmer(term), corpus_util.lemma(term)]
    return df


def check_word_stemmer(term, df_gsl_converted):
    df_aux_stemmer = df_gsl_converted[df_gsl_converted['stemmer'] == term]
    return len(df_aux_stemmer) == 0


def check_word_lemma(term, df_gsl_converted):
    df_aux_lemma = df_gsl_converted[df_gsl_converted['lemma'] == term]
    return len(df_aux_lemma) == 0


def download(df_01, type):
    df_01.to_csv(f'Data/Output/IPAVL_criterion_01_{type}.csv', index=False)
    print('-> A new file was generated: Data/Output/IPAVL_criterion_01_.csv')


def check_terms_stemmer(row, df_01_stemmer, df_gsl_converted):
    valid_word = check_word_stemmer(row['stemmer'], df_gsl_converted)
    if valid_word:
        df_01_stemmer.loc[len(df_01_stemmer)] = [row['term'], row['frequency'], row['stemmer'], row['lemma']]


def check_terms_lemma(row, df_01_lemma, df_gsl_converted):
    valid_word = check_word_stemmer(row['lemma'], df_gsl_converted)
    if valid_word:
        df_01_lemma.loc[len(df_01_lemma)] = [row['term'], row['frequency'], row['stemmer'], row['lemma']]


def start():
    df_gsl = pd.read_csv('Data/Input/GSL.csv')
    df_gsl_converted = convert_GSL(df_gsl)

    df_corpus = pd.read_csv('Data/Output/IPAVL.csv')
    df_01_stemmer = pd.DataFrame(columns=['term', 'frequency', 'stemmer', 'lemma'])
    df_01_lemma = pd.DataFrame(columns=['term', 'frequency', 'stemmer', 'lemma'])

    for i, row in df_corpus.iterrows():
        check_terms_stemmer(row, df_01_stemmer, df_gsl_converted)
        check_terms_lemma(row, df_01_lemma, df_gsl_converted)

    download(df_01_stemmer, 'stemmer')
    download(df_01_lemma, 'lemma')
