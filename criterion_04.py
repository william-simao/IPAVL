# Esta classe aplica o critério 04: familia da palavra
import pandas as pd


def check_family(df_c03, df_CPAVL, type):
    df = pd.DataFrame(columns=['lemma', 'term_frequency', 'family', 'family_length', 'term'])

    for i, row in df_c03.iterrows():
        df_aux = df_CPAVL[df_CPAVL[type] == row['term']]
        create_family(df, df_aux, type)

    return df


def create_family(df, df_aux, type):
    for i, row in df_aux.iterrows():
        df.loc[len(df)] = [row[type], row['frequency'], row['term'], len(df_aux), row['term']]


def create_dictionary():
    df_computing = pd.DataFrame(columns=["term", "lemma"])
    import corpus_util as corpus
    with open('Data/Input/terms_oxford_dictionary.txt', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            term = line.lower().replace("\n", "")
            df_computing.loc[len(df_computing)] = [term, corpus.lemma(term)]
    return df_computing


def check_dictionary(df, df_computing):
    df_c04_lemma = pd.DataFrame(columns=['token_IPAVL', 'token_IPAVL', 'token_oxford', 'lemma_oxford', 'frequency'])
    for i, row in df.iterrows():
        df_aux = df_computing[df_computing['term'] == row['term']]
        for i2, row2 in df_aux.iterrows():
            df_c04_lemma.loc[len(df_c04_lemma)] = [row['term'], row['lemma'], row2['term'], row2['lemma'], row['term_frequency']]
    df_c04_lemma.to_csv(r'Data/Output/IPAVL_criterion_04_lemma.csv', index=False)
    print('-> A new file was generated: Data/Output/IPAVL_criterion_04_lemma.csv')


def start():
    df_IPAVL = pd.read_csv('Data/Output/IPAVL.csv')
    df_c03_lemma = pd.read_csv('Data/Output/IPAVL_criterion_03_lemma.csv')
    df_c04_lemma = check_family(df_c03_lemma, df_IPAVL, 'lemma')
    df_computing = create_dictionary()
    check_dictionary(df_c04_lemma, df_computing)

