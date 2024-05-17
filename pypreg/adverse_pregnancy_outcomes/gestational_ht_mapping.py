"""
Codes sourced from

Bateman BT, Mhyre JM, Hernandez-Diaz S, Huybrechts KF, Fischer MA, Creanga AA, Callaghan WM, Gagne JJ.
    Development of a comorbidity index for use in obstetric patients. Obstet Gynecol. 2013 Nov;122(5):957-965.
    doi: 10.1097/AOG.0b013e3182a603bb. PMID: 24104771; PMCID: PMC3829199
Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK.
    An Expanded Obstetric Comorbidity Scoring System for Predicting Severe Maternal Morbidity. Obstet Gynecol.
    2020 Sep;136(3):440-449. doi: 10.1097/AOG.0000000000004022. PMID: 32769656; PMCID: PMC7523732
"""

import pandas as pd

ght = dict()

type = 'DX'
version = 'ICD9'
code = 'code'

ght[type] = dict()
ght[type][version] = dict()
ght[type][version][code] = (
    "^6423.*",
)

version = 'ICD10'
ght[type][version] = dict()
ght[type][version][code] = (
    "^O13.*",
)


ght = pd.DataFrame.from_dict(ght, orient='index').stack().to_frame()
ght = pd.DataFrame(ght[0].values.tolist(), index=ght.index)
ght = pd.DataFrame(ght[code].values.tolist(), index=ght.index).stack().reset_index().drop('level_2', axis=1)

ght.columns = ['type', 'version', 'code']
