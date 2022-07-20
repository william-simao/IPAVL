# Esta classe aplica o critério 02: propósito não acadêmico
# Atenção! Os arquivos usados do diretório "Input" estão no projeto "corpus BNC"
import pandas as pd

# region stemmer
def check_BNC_stemmer(df_bnc, row):
    df_bnc_aux = df_bnc[df_bnc['stemmer'] == row['stemmer']] # Verifica no corpus da BNC há o termo do meu corpus
    frequency = 0
    for i, row_bnc in df_bnc_aux.iterrows():
        frequency = frequency + row_bnc['frequency']
    return frequency # retorna a frequência do termo


def calcule_BNC_stemmer(frequency, bnc_length):
    return float(frequency * 100 / bnc_length)


def bnc_stemmer_process(df_bnc, bnc_length, df_c01_stemmer):
    cpavl_length_c01_stemmer = df_c01_stemmer['frequency'].sum()
    df = pd.DataFrame(columns=['term', 'frequency', 'stemmer', 'frequency_BNC', 'frequency_CPAVL', 'frequency_ratio'])
    for i, row in df_c01_stemmer.iterrows():
        # verifica a frequência no corpus da BNC
        frequency_BNC = calcule_BNC_stemmer(check_BNC_stemmer(df_bnc, row), bnc_length)

        # verifica a frequência da palavra no meu corpus (CSAVL)
        frequency_CPAVL = float(row['frequency'] * 100 / cpavl_length_c01_stemmer)

        # The frequency of a lemma in CSAC1 must be 150% that of its frequency in a corpus of general English
        frequency_ratio = frequency_BNC * 150 / 100
        if frequency_CPAVL >= frequency_ratio:
            df.loc[len(df)] = [row['term'], row['frequency'], row['stemmer'], frequency_BNC, frequency_CPAVL, frequency_ratio]

    return df
#endregion


# region lemma
def check_BNC_lemma(df_bnc, row):
    df_bnc_aux = df_bnc[df_bnc['lemman'] == row['lemma']] # Verifica no corpus da BNC há o termo do meu corpus
    frequency = 0
    for i, row_bnc in df_bnc_aux.iterrows():
        frequency = frequency + row_bnc['frequency']
    return frequency # retorna a frequência do termo


def calcule_BNC_lemma(frequency, bnc_length):
    return float(frequency * 100 / bnc_length)


def bnc_lemma_process(df_bnc, bnc_length, df_c01_lemma):
    cpavl_length_c01_lemma = df_c01_lemma['frequency'].sum()
    df = pd.DataFrame(columns=['term', 'frequency', 'lemma', 'frequency_BNC', 'frequency_CPAVL', 'frequency_ratio'])
    for i, row in df_c01_lemma.iterrows():
        # verifica a frequência no corpus da BNC
        frequency_BNC = calcule_BNC_lemma(check_BNC_lemma(df_bnc, row), bnc_length)

        # verifica a frequência da palavra no meu corpus (CSAVL)
        frequency_CPAVL = float(row['frequency'] * 100 / cpavl_length_c01_lemma)

        # The frequency of a lemma in CSAC1 must be 150% that of its frequency in a corpus of general English
        frequency_ratio = frequency_BNC * 150 / 100
        if frequency_CPAVL >= frequency_ratio:
            df.loc[len(df)] = [row['term'], row['frequency'], row['lemma'], frequency_BNC, frequency_CPAVL, frequency_ratio]
        else:
            print(row['term'])

    return df
#endregion


def start():
    df_bnc = pd.read_csv('Data/Input/BNC_corpus_unified.csv')
    bnc_length = df_bnc['frequency'].sum()

    #df_c01_stemmer = pd.read_csv('Data/Output/CPAVL_criterion_01_stemmer.csv')
    #df_c02_stemmer = bnc_stemmer_process(df_bnc, bnc_length, df_c01_stemmer)

    #df_c02_stemmer.to_csv(r'Data/Output/CPAVL_criterion_02_stemmer.csv', index=False)
    #print('-> A new file was generated: Data/Output/CPAVL_criterion_02_stemmer.csv')

    df_c01_lemma = pd.read_csv('Data/Output/IPAVL_criterion_01_lemma.csv')
    df_c02_lemma = bnc_lemma_process(df_bnc, bnc_length, df_c01_lemma)

    df_c02_lemma.to_csv(r'Data/Output/IPAVL_criterion_02_lemma.csv', index=False)
    print('-> A new file was generated: Data/Output/CPAVL_criterion_02_lemma.csv')