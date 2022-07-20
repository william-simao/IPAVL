from urllib.request import urlopen
import pandas as pd


def start():
    df = pd.read_csv('Data/Output/IPAVL_criterion_04_lemma.csv')
    df_definition = pd.DataFrame(columns=['token_IPAVL', 'lemma_CPAVL', 'definition'])
    for i, row in df.iterrows():
        print(row['token_CPAVL'])
        definition = request(row['token_CPAVL'])
        df_definition.loc[len(df_definition)] = [row['token_CPAVL'], row['lemma_CPAVL'], definition]
    df_definition.to_csv(r'Data/Output/IPAVL_criterion_04_lemma_definition.csv', index=False)
    print('-> A new file was generated: Data/Output/IPAVL_criterion_04_lemma_definition.csv')


def request(token):
    from bs4 import BeautifulSoup
    from urllib.error import HTTPError
    try:
        html = urlopen(f'https://en.wiktionary.org/w/index.php?title={token}')
        html_result = BeautifulSoup(html.read(), "html.parser")
        html_text = html_result.get_text()
        html_lines = html_text.split("\n")
        for line in html_lines:
            if line.startswith("(programming)"):
                return line
            if "comput" in line:
                return "(comput-) " + line
            if "informatic" in line:
                return "(informatic-)" + line
    except HTTPError as e:
        return ""
    return ""