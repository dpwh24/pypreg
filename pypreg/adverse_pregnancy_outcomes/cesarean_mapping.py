"""
Codes sourced from:

Agency for Healthcare Research and Quality: https://qualityindicators.ahrq.gov/Downloads/Modules/IQI/V50-ICD10/TechSpecs/IQI%2021%20Cesarean%20Delivery%20Rate,%20Uncomplicated.pdf

Castillo, Wendy Camelo / Boggess, Kim / Stürmer, Til / Brookhart, M. Alan / Benjamin, Daniel K. / Funk, Michele Jonsson
    Trends in Glyburide Compared With Insulin Use for Gestational Diabetes Treatment in the United States, 2000-2011
    Obstetrics & Gynecology , Vol. 123, No. 6 Ovid Technologies (Wolters Kluwer Health) p. 1177-1184

And code search using keyword "cesar" and including any procedure which indicates cesarean was performed
"""

import pandas as pd

cesarean = dict()

type = 'PX'
version = 'ICD9'
code = 'code'

cesarean[type] = dict()
cesarean[type][version] = dict()
cesarean[type][version][code] = (
    "^74([0-24]|99)$", #74.9 excluded as child code should be used (could also describe hysterotomy 74.91
)

version = 'ICD10'
cesarean[type][version] = dict()
cesarean[type][version][code] = (
    "^10D00Z[0-2]$",
)

version = 'CPT4'
cesarean[type][version] = dict()
cesarean[type][version][code] = (
    "^00857$",
    "^58611$",
    "^5950[01]$",
    "^5951[0-5]$",
    "^5952[015]$",
    "^5954[01]$",
    "^59618$",
    "^5962[02]$",
    "^0196[1389]$",
)

type = 'DX'
cesarean[type] = dict()
version = 'ICD9'
cesarean[type][version] = dict()
cesarean[type][version][code] = (
    "^6498.*",
    "^6697.*",
    "^6741.*",
    "^V3[0-79]01$",
    "^7634$",
)

version = 'ICD10'
cesarean[type][version] = dict()
cesarean[type][version][code] = (
    "^O82$",
    "^O7582$",
    "^Z38([03]1|6[2469])$",
    "^O900$",
    "^P034$",
)

type = 'DRG'
cesarean[type] = dict()
version = 'DRG'
cesarean[type][version] = dict()
cesarean[type][version][code] = (
    "^37[01]$",
    "^76[56]$",
)

cesarean = pd.DataFrame.from_dict(cesarean, orient='index').stack().to_frame()
cesarean = pd.DataFrame(cesarean[0].values.tolist(), index=cesarean.index)
cesarean = pd.DataFrame(cesarean[code].values.tolist(), index=cesarean.index).stack().reset_index().drop('level_2', axis=1)

cesarean.columns = ['type', 'version', 'code']
