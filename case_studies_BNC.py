import pandas as pd


# Verifica quais termos da IPAVL estão no BNC
def check(df_bnc, df_ipavl):
    df = pd.DataFrame(columns=['lemma', 'BNC term', 'BNC term frequency'])
    for i, row in df_bnc.iterrows():
        print(f'processando {i} de 38885...')
        for i2, row2 in df_ipavl.iterrows():
            if row2['lemma'] == row['lemman']:
                if check_term(df, row['term']):
                    df.loc[len(df)] = [row2['lemma'], row['term'], row['frequency']]
    return df


# Verifica se o termo já foi identificado
def check_term(df, term):
    for i, row in df.iterrows():
        if row['lemma'] is term:
            return False
    return True


def start(df_ipavl):
    df_bnc = pd.read_csv('Data/Input/Case Studies/BNC_aca_converted.csv')
    df = check(df_bnc, df_ipavl)
    df.to_csv(f'Data/Output/Case Studies/BNC_aca.csv', index=False)
    print('-> A new file was generated: Data/Output/Case Studies/BNC_aca.csv')


def start_comparision(df_ipavl):
    df_bnc = pd.read_csv('Data/Output/Case Studies/BNC_aca.csv')
    df = pd.DataFrame(columns=['lemma', 'has'])
    for i, row in df_ipavl.iterrows():
        has = False
        for i2, row2 in df_bnc.iterrows():
            if row2['lemma'] == row['lemma']:
                has = True
                break
        df.loc[i] = [row['lemma'], has]

    df.to_csv(f'Data/Output/Case Studies/BNC_aca_comparision.csv', index=False)
    print('-> A new file was generated: Data/Output/Case Studies/BNC_aca_comparision.csv')

