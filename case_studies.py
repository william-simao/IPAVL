import pandas as pd


def get_IPAVL():
    df_aux = pd.read_csv('Data/Output/Case studies/IPAVL_Processed.csv')
    df = pd.DataFrame(columns=["lemma"])
    for i, row in df_aux.iterrows():
        if row['Status'] == 'Valid':
            df.loc[len(df)] = [row['lemma_IPAVL']]
    # print(len(df))
    # print(df.to_string())
    return df

# region CSAVL-S
def start_csavl_s():
    csavl_s = load_csavl('CSAVL-S.txt')
    list_csavl = process_csavl(csavl_s)
    df = get_IPAVL()
    check(df, list_csavl, '01-CPAVL-S.csv')
# endregion

# region CSAVL
def start_csavl():
    csavl = load_csavl('CSAVL.txt')
    list_csavl = process_csavl(csavl)
    write_corpus('CSAVL.txt', list_csavl)

    df = get_IPAVL()
    check(df, list_csavl, '01-CPAVL.csv')


def load_csavl(name):
    f = open("Data/Input/Case Studies/" + name, "r", encoding="utf8")
    return f.read()


def process_csavl(csavl):
    list = []
    for term in csavl.split('\n'):
        term_aux = get_start(term)
        term_aux2 = get_end(term_aux)
        final_term = get_term(term_aux2)
        list.append(final_term)
        #print(term, final_term)
    return list

# o termo vem a linha, asterisco (opcional) e se é verbo, adjetivo, etc... Ex: 904 leverage_v
# Por isso mesmo, neste método eu faço um split no espaço para remover linha e asterisco (se houver)
def get_start(term):
    return term.split(' ')


# Aqui eu removo a linha e o espaço, continuando o método get_start()
def get_end(term_aux):
    return term_aux[len(term_aux) - 1]


# Aqui eu pego o termo, eliminando o que vem depois do underline
def get_term(term_aux2):
    return term_aux2.split('_')[0]


def check(df, csavl, name):
    df_csavl = pd.DataFrame(columns=['lemma'])
    for i, row in df.iterrows():
        for term in csavl:
            if term == row['lemma']:
                df_csavl.loc[len(df_csavl)] = [term]
    df_csavl.to_csv(f'Data/Output/Case Studies/' + name, index=False)
    print('-> A new file was generated: Data/Output/Case Studies/' + name)

# endregion


# region CSWL
def start_CSWL():
    file = load_cswl()
    lst_cswl = process_cswl(file)

    df = get_IPAVL()
    df_cswl = pd.DataFrame(columns=["lemma", "term_CSWL"])
    for i, row in df.iterrows():
        for term in lst_cswl:
            if term == row['lemma']:
                df_cswl.loc[len(df_cswl)] = [row['lemma'], term]
    df_cswl.to_csv(f'Data/Output/Case Studies/CSWL.csv', index=False)
    print('-> A new file was generated: Data/Output/Case Studies/CSWL.csv')


def load_cswl():
    f = open("Data/Input/Case Studies/CSWL.txt", "r", encoding="utf8")
    return f.read()


def process_cswl(file):
    lst_cswl = []
    for row in file.split('\n'):
        lst_cswl.append(row.strip())
    return lst_cswl
#endregion


#region AWL
def start_AWL():
    file = load_awl()
    lst_awl = process_awl(file)

    df = get_IPAVL()
    df_awl = pd.DataFrame(columns=["lemma", "term_AWL"])
    for i, row in df.iterrows():
        for term in lst_awl:
            if term == row['lemma']:
                df_awl.loc[len(df_awl)] = [row['lemma'], term]
    df_awl.to_csv(f'Data/Output/Case Studies/AWL.csv', index=False)
    print('-> A new file was generated: Data/Output/Case Studies/AWL.csv')


def load_awl():
    f = open("Data/Input/Case Studies/awl.txt", "r", encoding="utf8")
    return f.read()


def process_awl(file):
    import corpus_util as corpus_util
    lst_cswl = []
    for row in file.split('\n'):
        lst_cswl.append(corpus_util.lemma(row.strip().split(' ')[0]))
    return lst_cswl
#endregion


#region AVL
def start_AVL():
    file = load_avl()
    lst_avl = process_avl(file)

    df = get_IPAVL()
    df_avl = pd.DataFrame(columns=["lemma", "term_AVL"])
    for i, row in df.iterrows():
        for term in lst_avl:
            if term == row['lemma']:
                df_avl.loc[len(df_avl)] = [row['lemma'], term]
    df_avl.to_csv(f'Data/Output/Case Studies/AVL.csv', index=False)
    print('-> A new file was generated: Data/Output/Case Studies/AVL.csv')


def load_avl():
    f = open("Data/Input/Case Studies/avl.txt", "r", encoding="utf8")
    return f.read()


def process_avl(file):
    import corpus_util as corpus_util
    lst_avl = []
    for row in file.split('\n'):
        lst_avl.append(corpus_util.lemma(row.split('.')[1].strip()))
    return lst_avl
#endregion

def write_corpus(name, list):
    file = open("Data/Output/Case studies/" + name, "w", encoding="utf-8")
    for word in list:
        file.write(word + "\n")
    file.close()
    print('-> A new file was generated: Data/Output/Case Studies/' + name)


def start():
    import case_studies_BNC as bnc
    # bnc.start(get_IPAVL())
    # bnc.start_comparision(get_IPAVL()) # compara quais termos tem na IPAVL e na BNC

    # start_AWL()
    # start_AVL()

    start_CSWL()
    start_csavl()
    start_csavl_s()