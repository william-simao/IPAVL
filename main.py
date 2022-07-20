import corpus as corpus
import corpus_util as corpus_util

start_corpus = False
start_corpus_util = False
start_criteria_01 = False
start_criteria_02 = False
start_criteria_03 = False
start_criteria_04 = False
start_definitions = False
start_data_formatter = False
start_case_studies = False
start_case_study_merlot = True


if start_corpus:
    corpus.start()

if start_corpus_util:
    corpus_util.start()

if start_criteria_01:
    print('-- Criterion 01 started --')
    import criterion_01 as criterion_01
    criterion_01.start()
    print('-- Criterion 01 finished --')

if start_criteria_02:
    print('-- Criterion 02 started --')
    import criterion_02 as criterion_02
    criterion_02.start()
    print('-- Criterion 02 finished --')

if start_criteria_03:
    print('-- Criterion 03 started --')
    import criterion_03 as criterion_03
    criterion_03.start()
    print('-- Criterion 03 finished --')

if start_criteria_04:
    print('-- Criterion 04 started --')
    import criterion_04 as criterion_04
    criterion_04.start()
    print('-- Criterion 04 finished --')

if start_definitions:
    print('-- Definition started --')
    import definitions as definition
    definition.start()
    print('-- Definition finished --')

if start_data_formatter:
    print('-- Data Formatter started --')
    import data_formatter as data_formatter
    data_formatter.start()
    print('-- Data Formatter finished --')

if start_case_studies:
    print('-- Case Studies started --')
    import case_studies as casestudies
    casestudies.start()
    print('-- Case Studies finished --')

if start_case_study_merlot:
    print('-- Case Studies Merlot started --')
    import case_study_Merlot as merlot
    merlot.start()
    print('-- Case Studies Merlot  finished --')

