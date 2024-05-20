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

gdm = dict()

type = 'DX'
version = 'ICD9'
code = 'CODE'

gdm[type] = dict()
gdm[type][version] = dict()
gdm[type][version][code] = (
    "^6488.*",
)

version = 'ICD10'
gdm[type][version] = dict()
gdm[type][version][code] = (
    "^O244.*",
    "^O9981.*",
)


gdm = pd.DataFrame.from_dict(gdm, orient='index').stack().to_frame()
gdm = pd.DataFrame(gdm[0].values.tolist(), index=gdm.index)
gdm = pd.DataFrame(gdm[code].values.tolist(), index=gdm.index).stack().reset_index().drop('level_2', axis=1)

gdm.columns = ['code_type', 'VERSION', 'CODE']
