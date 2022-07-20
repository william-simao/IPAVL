# CLASSE ANTIGA, EM DESUSO

import math

import pandas as pd
# Essa classe aplica os critérios para seleção de palavras

BNC_CORPUS_LENGTH = 2990971 # Tamanho do corpus da BNC sem incluir a parte acadêmica
CPAVL_CORPUS_LENGTH = 195181 # Tamanho do corpus que eu gerei
CPAVL_CORPUS_LENGTH_C01 = 188221 # Tamanho do corpus que estou gerei (criterion 01)
CPAVL_CORPUS_LENGTH_C02 = 0 # Tamanho do corpus que estou gerei (criterion 02)


# region criterion 01 (min length)
def criterion_01():
    df = pd.read_csv('Data/Output/CPAVL.csv')
    df_01 = pd.DataFrame(columns=['term', 'frequency'])
    min = CPAVL_CORPUS_LENGTH * 0.0028 / 100
    for i, row in df.iterrows():
        if row['frequency'] > min:
            df_01.loc[len(df_01)] = [row['term'], row['frequency']]

    df_01.to_csv(r'Data/Output/CPAVL_criterion_01.csv', index=False)
    print('-> A new file was generated: Data/Output/CPAVL_criterion_01.csv')
    print('-> CSAVL_length: ', CPAVL_CORPUS_LENGTH_C01)
# endregion

# region criterion 02 (Non academic purpose)
def criterion_02(start_bnc):
    if start_bnc:
        import criterion_02 as criterion_02
        criterion_02.start()

    df_02 = pd.DataFrame(columns=['term', 'frequency', 'frequency_ratio_BNC', 'frequency_ratio_CPAVL', 'frequency_ratio'])
    df = pd.read_csv('Data/Output/CPAVL_criterion_01.csv')
    df_bnc = load_BNC()

    for i, row in df.iterrows():
        frequency_ratio_BNC = check_BNC(df_bnc, row)
        frequency_ratio_CPAVL = float(row['frequency'] * 100 / CPAVL_CORPUS_LENGTH_C01) # verifica a frequência da palavra no meu corpus (CSAVL)
        frequency_ratio = frequency_ratio_BNC * 150 / 100
        if frequency_ratio_CPAVL >= frequency_ratio: # The frequency of a lemma in CSAC1 must be 150% that of its frequency in a corpus of general English
            df_02.loc[len(df_02)] = [row['term'], row['frequency'], frequency_ratio_BNC, frequency_ratio_CPAVL, frequency_ratio]
    print('CSVAL Length (Criterion 02): ', df_02.frequency.sum(axis=0))
    df_02.to_csv(r'Data/Output/CPAVL_criterion_02.csv', index=False)
    print('-> A new file was generated: Data/Output/CPAVL_criterion_02.csv')


# Este método carrega os 3 corpus da BNC em apenas 1 dataframe
def load_BNC():
    df_bnc = pd.DataFrame(columns=['term', 'frequency'])

    df_dem = pd.read_csv('Data/Output/BNC_dem.csv')
    df_fic = pd.read_csv('Data/Output/BNC_fic.csv')
    df_news = pd.read_csv('Data/Output/BNC_news.csv')
    print('> load_BNC() started <')
    for i, row in df_dem.iterrows():
        df_bnc.loc[len(df_bnc)] = [row['term'], row['frequency']]
    for i, row in df_fic.iterrows():
        df_bnc.loc[len(df_bnc)] = [row['term'], row['frequency']]
    for i, row in df_news.iterrows():
        df_bnc.loc[len(df_bnc)] = [row['term'], row['frequency']]
    print('> load_BNC() finished <')
    print('BNC corpus length: ', df_bnc.frequency.sum(axis=0))
    return df_bnc


# Este método recebe o corpus da BNC e a linha do meu corpus (CPAVL)
def check_BNC(df_bnc, row):
    df_bnc_aux = df_bnc[df_bnc['term'] == row['term']] # Verifica no corpus da BNC há o termo do meu corpus
    frequency = 0
    for i, row_bnc in df_bnc_aux.iterrows():
        frequency = frequency + row_bnc['frequency']
    return float(frequency * 100 / BNC_CORPUS_LENGTH) # Se houver, verifica a proporção
# endregion


# region criterion 03 (Popular words)
def criterion_03():
    df_gsl = pd.read_csv('Data/Input/GSL.csv')
    df = pd.read_csv('Data/Output/CPAVL_criterion_02.csv')
    df_03 = pd.DataFrame(columns=['term', 'frequency'])
    for i, row in df.iterrows():
        is_valid = True
        for i2, row2 in df_gsl.iterrows():
            import corpus_util as corpus_util
            stemmer_word = corpus_util.stemmer(row2['Lemma'])
            if row['term'] == stemmer_word:
                is_valid = False
                break
        if is_valid:
            df_03.loc[len(df_03)] = [row['term'], row['frequency']]
    df_03.to_csv(r'Data/Output/CPAVL_criterion_03.csv', index=False)
    print('-> A new file was generated: Data/Output/CPAVL_criterion_03.csv')


# endregion

# region criterion 04
def check_word_family(df_cpavl_aux, row):
    return df_cpavl_aux[df_cpavl_aux['term_stemmer'] == row['term']]


def count_word_family(df_aux):
    from collections import Counter
    counter = Counter(df_aux['term'])
    return counter.items()


def criterion_04():
    df_04 = pd.DataFrame(columns=['term', 'word_family_length', 'word_family', 'frequency'])
    df = pd.read_csv('Data/Output/CPAVL_criterion_03.csv')
    df_cpavl_aux = pd.read_csv('Data/Output/CPAVL_aux.csv')

    for i, row in df.iterrows():
        df_aux = check_word_family(df_cpavl_aux, row)
        dict_terms = count_word_family(df_aux)
        for terms in dict_terms:
            df_04.loc[len(df_04)] = [row['term'], len(dict_terms), terms[0], terms[1]]

    df_04.to_csv(r'Data/Output/CPAVL_criterion_04.csv', index=False)
    print('-> A new file was generated: Data/Output/CPAVL_criterion_04.csv')
#endregion


def start():
    print('-- Criteria Started --')
    #criterion_01()
    #criterion_02(False)
    criterion_03()
    criterion_04()
    print('-- Criteria Finished --')
