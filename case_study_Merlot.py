import pandas as pd


# region processa as requisições dos REA
def requisition(seed):
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.error import URLError
    from bs4 import BeautifulSoup

    try:
        html = urlopen(str(seed))
    except HTTPError as e:
        print(e)
        return False
    except URLError:
        print("Server down or incorrect domain")
        return False
    else:
        return BeautifulSoup(html.read(), "html.parser")


def make_requests(df_oer, df_oer_processed):
    for i, row in df_oer.iterrows():
        print(f'link: {i}')
        result = requisition(row['Chapter link'])
        process_result(result, row, df_oer_processed)


def process_result(result, row, df_oer_processed):
    import corpus as corpus
    import corpus_util as corpus_util
    lst_terms = corpus.clean_text(result.getText())
    for term in lst_terms:
        lemma = corpus_util.lemman(term)
        df_oer_processed.loc[len(df_oer_processed)] = [term, lemma, row['Book'], row['Chapter name'], row['CS']]
    df_oer_processed.to_csv(f'Data/Output/Case Studies/OER Processed.csv', index=False)
    print('-> A new file was generated/updated: Data/Output/Case Studies/OER Processed.csv')


def start_process():
    df_oer_processed = pd.DataFrame(columns=['term', 'lemma', 'book', 'chapter', 'cs'])
    df_oer = pd.read_csv('Data/Input/Case Studies/oer.csv')
    make_requests(df_oer, df_oer_processed)
# endregion


# region compara os termos do vocabulário com os REA
def get_IPAVL():
    df_aux = pd.read_csv('Data/Output/Case studies/IPAVL_Processed.csv')
    df = pd.DataFrame(columns=["lemma"])
    for i, row in df_aux.iterrows():
        if row['Status'] == 'Valid':
            df.loc[len(df)] = [row['lemma_IPAVL']]
    # print(len(df))
    # print(df.to_string())
    return df


def start_comparation():
    df_oer = pd.read_csv('Data/Output/Case studies/OER Processed.csv')
    df_terms = get_IPAVL()
    df = pd.DataFrame(columns=['IPAVL Lemma', 'OER Token', 'OER Lemma', 'Book', 'Chapter', 'CS'])
    for i, row in df_terms.iterrows():
        print(f'terms processed {i+1}/230')
        df_aux = df_oer[df_oer.lemma == row['lemma']]
        for i2, row2 in df_aux.iterrows():
            df.loc[len(df)] = [row['lemma'], row2['term'], row2['lemma'], row2['book'], row2['chapter'], row2['cs']]

    df.to_csv(f'Data/Output/Case Studies/OER Processed Terms.csv', index=False)
    print('-> A new file was generated/updated: Data/Output/Case Studies/OER Processed Terms.csv')
# endregion


def start_check():
    df_oer = pd.read_csv('Data/Output/Case studies/OER Processed.csv')
    df_oer_terms = pd.read_csv('Data/Output/Case studies/OER Processed Terms.csv')
    df = pd.DataFrame(columns=['term', 'lemma', 'frequency'])

    df_aux = df_oer[df_oer['chapter'] == 'Introduction']
    df_aux2 = df_oer_terms[df_oer['chapter'] == 'Introduction']
    print(df_aux2, df_aux)


def start():
    # start_process() # Se precisar ler novos links para criar as listas
    # start_comparation() # Se precisar comparar novos links processados com os termos
    # start_check()
    metric_4()
    metric_5()


def metric_4():
    df_oer = pd.read_csv('Data/Output/Case studies/OER Processed.csv')
    df_oer_processed = pd.read_csv('Data/Output/Case studies/OER Processed Terms.csv')
    df_introductory_total = get_introductory(df_oer, "cs")
    df_introductory_IPAVL = get_introductory(df_oer_processed, "CS")

    df_advanced_total = get_advanced(df_oer, "cs")
    df_advanced_IPAVL = get_advanced(df_oer_processed, "CS")

    print('MÉTRICA 04')
    print('Classification;Lemmas (total);IPAVL Lemmas (total)')
    print(f'Introductory;{len(df_introductory_total)};{len(df_introductory_IPAVL)}')
    print(f'Advanced;{len(df_advanced_total)};{len(df_advanced_IPAVL)}')
    print('')
    print('Classification;Lemmas (total);IPAVL Lemmas (total)')
    print(f'Introductory;{len(set(df_introductory_total["lemma"]))};{len(set(df_introductory_IPAVL["IPAVL Lemma"]))}')
    print(f'Advanced;{len(set(df_advanced_total["lemma"]))};{len(set(df_advanced_IPAVL["IPAVL Lemma"]))}')
    print('')


def get_introductory(df, column):
    return df[df[column] == 1]


def get_advanced(df, column):
    return df[df[column] == 2]


def metric_5():
    df_oer = pd.read_csv('Data/Output/Case studies/OER Processed.csv')
    df_oer_processed = pd.read_csv('Data/Output/Case studies/OER Processed Terms.csv')

    df_introductory_total = get_introductory(df_oer, "cs")
    df_introductory_IPAVL = get_introductory(df_oer_processed, "CS")

    df_advanced_total = get_advanced(df_oer, "cs")
    df_advanced_total_balanced = pd.DataFrame(columns=["lemma"])
    get_balanced(df_advanced_total, "chapter", df_advanced_total_balanced, 1)

    df_advanced_IPAVL = get_advanced(df_oer_processed, "CS")
    df_advanced_IPAVL_balanced = pd.DataFrame(columns=['IPAVL Lemma'])
    get_balanced(df_advanced_IPAVL, "Chapter", df_advanced_IPAVL_balanced, 0)

    print('MÉTRICA 5')
    print('Classification;Lemmas (total);IPAVL Lemmas (total)')
    print(f'Introductory;{len(df_introductory_total)};{len(df_introductory_IPAVL)}')
    print(f'Advanced;{len(df_advanced_total_balanced)};{len(df_advanced_IPAVL_balanced)}')
    print('')
    print('Classification;Lemmas (total);IPAVL Lemmas (total)')
    print(f'Introductory;{len(set(df_introductory_total["lemma"]))};{len(set(df_introductory_IPAVL["IPAVL Lemma"]))}')
    print(f'Advanced;{len(set(df_advanced_total_balanced["lemma"]))};{len(set(df_advanced_IPAVL_balanced["IPAVL Lemma"]))}')
    print('')
    print(set(df_introductory_IPAVL["IPAVL Lemma"]))
    print(set(df_advanced_IPAVL_balanced["IPAVL Lemma"]))

def get_balanced(df, column, df_oer_processed, id_row):
    for i, row in df.iterrows():
        if row[column] == 'Asynchronous Programming':
            df_oer_processed.loc[len(df_oer_processed)] = [row[id_row]]
        if row[column] == 'Drawing on Canvas':
            df_oer_processed.loc[len(df_oer_processed)] = [row[id_row]]
        if row[column] == 'Handling Events':
            df_oer_processed.loc[len(df_oer_processed)] = [row[id_row]]
        if row[column] == 'Higher-order Functions':
            df_oer_processed.loc[len(df_oer_processed)] = [row[id_row]]
        if row[column] == 'HTTP and Forms':
            df_oer_processed.loc[len(df_oer_processed)] = [row[id_row]]
        if row[column] == 'Project: A Programming Language':
            df_oer_processed.loc[len(df_oer_processed)] = [row[id_row]]
        if row[column] == 'Project: A Robot':
            df_oer_processed.loc[len(df_oer_processed)] = [row[id_row]]