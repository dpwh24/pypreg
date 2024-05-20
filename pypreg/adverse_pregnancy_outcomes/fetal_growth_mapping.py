"""
Codes identified through CODE search of ICD-10 and crosswalk to ICD-9
"""

import pandas as pd

fg = dict()

type = 'DX'
version = 'ICD9'
code = 'CODE'

fg[type] = dict()
fg[type][version] = dict()
fg[type][version][code] = (
    "^6565.*",
)

version = 'ICD10'
fg[type][version] = dict()
fg[type][version][code] = (
    "^O3659.*",
)


fg = pd.DataFrame.from_dict(fg, orient='index').stack().to_frame()
fg = pd.DataFrame(fg[0].values.tolist(), index=fg.index)
fg = pd.DataFrame(fg[code].values.tolist(), index=fg.index).stack().reset_index().drop('level_2', axis=1)

fg.columns = ['code_type', 'VERSION', 'CODE']
