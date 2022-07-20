# Esta classe aplica o critério 03: frequência mínima
import pandas as pd


def get_keys(lst_keys, df_c02, type):
    df = pd.DataFrame(columns=['term', 'frequency'])
    for key in lst_keys:
        df_aux = df_c02[df_c02[type] == key]
        frequency = df_aux['frequency'].sum()
        df.loc[len(df)] = [key, frequency]
    return df


def count_word_family(df, type):
    from collections import Counter
    counter = Counter(df[type])
    return counter.keys()


def check_frequency(df_c03, min_frequency):
    df = pd.DataFrame(columns=['term', 'frequency'])
    for i, row in df_c03.iterrows():
        if row['frequency'] >= min_frequency:
            df.loc[len(df)] = [row['term'], row['frequency']]

    return df


def start():
    # Este é o meu paramêtro de corpus oriundo do estudo "A Computer Science Academic Vocabulary List"
    CSAVL_length = 3532486

    #df_c02_stemmer = pd.read_csv('Data/Output/CPAVL_criterion_02_stemmer.csv')
    #lst_stemmers = count_word_family(df_c02_stemmer, 'stemmer')
    #df_c03_stemmer_keys = get_keys(lst_stemmers, df_c02_stemmer, 'stemmer')

    # Aqui eu calculo a frequência considerando a proporção do estudo de referência
    #min_frequency = df_c03_stemmer_keys['frequency'].sum() * 100 / CSAVL_length
    #df_c03_stemmer = check_frequency(df_c03_stemmer_keys, min_frequency)

    #df_c03_stemmer.to_csv(r'Data/Output/IPAVL_criterion_03_stemmer.csv', index=False)
    #print('-> A new file was generated: Data/Output/IPAVL_criterion_03_stemmer.csv')


    df_c02_lemma = pd.read_csv('Data/Output/IPAVL_criterion_02_lemma.csv')
    lst_lemma = count_word_family(df_c02_lemma, 'lemma')
    df_c03_lemma_keys = get_keys(lst_lemma, df_c02_lemma, 'lemma')

    # Aqui eu calculo a frequência considerando a proporção do estudo de referência
    min_frequency = df_c03_lemma_keys['frequency'].sum() * 100 / CSAVL_length
    df_c03_lemma = check_frequency(df_c03_lemma_keys, min_frequency)

    df_c03_lemma.to_csv(r'Data/Output/IPAVL_criterion_03_lemma.csv', index=False)
    print('-> A new file was generated: Data/Output/IPAVL_criterion_03_lemma.csv')
