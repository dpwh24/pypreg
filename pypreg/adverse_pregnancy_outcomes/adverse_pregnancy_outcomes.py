"""
Adverse Pregnancy Outcomes

Author:
Dave Walsh 22 Aug 2023
Department of Biomedical and Health Informatics
UMKC

Looks at a pandas dataframe containing diagnositic, procedure, and DRG codes to report out the presence of
Cesarean section, Fetal growth restriction, Gestation Diabetes, Gestational Hypertension, and Preeclampsia.
The function accepts codes from ICD9, ICD10, DRG, and CPT coding systems.
"""


import pandas as pd
import warnings
from .cesarean_mapping import cesarean
from .fetal_growth_mapping import fg
from .gestational_dm_mapping import gdm
from .gestational_ht_mapping import ght
from .preeclampsia_mapping import pe


def apo(df: pd.DataFrame,
        patient_id: str,
        preg_id: str,
        type: str,
        version: str,
        code: str):
    """
    Main function
    :param df: Pandas dataframe that contains encounter level data for each pregnancy, rows should be unique to each
    code for a given encounter
    :param patient_id: Column containing the unique patient identifier
    :param preg_id: Column containing the pregnancy identifier
    :param type: Column containing if the code describes a procedure, diagnosis, or DRG
    :param version: Column containing the coding system for the provided code
    :param code: Column containing the code

    :return: Returns a pandas dataframe containing patient and pregnancy identifiers with boolean columns for
        - cesarean
        - fetal growth restriction
        - gestational diabete
        - gestational hypertension
        - preeclampsia
    """

    # Error checking to ensure the reported columns are contained in the dataframe
    if not {patient_id, preg_id, type, version, code}.issubset(df.columns):
        raise KeyError(f"Ensure that columns {[patient_id, preg_id, type, version, code]} are present in the data.")

    package_cols = {patient_id: 'patient_sk',
                    preg_id: 'preg_id',
                    version: 'version',
                    type: 'type',
                    code: 'code'
                    }
    restore_cols = {i: j for j, i in package_cols.items()}

    # Refactor the passed column names
    patient_id = package_cols[patient_id]
    preg_id = package_cols[preg_id]
    version = package_cols[version]
    type = package_cols[type]
    code = package_cols[code]

    df.rename(columns=package_cols, inplace=True)

    # Types can accept a code label as dx/diagnosis or px/procedure
    types = dict()
    types['DX'] = ('dx',
                   'diagnosis')
    types['PX'] = ('px',
                   'procedure')
    types['DRG'] = ('drg',
                    'diagnostic related group',
                    'diagnostic grouping')

    # Versions can accept different coding systems: 9/ICD9, 10/ICD10/ICD10-CM/ICD10-PCS, DRG
    versions = dict()
    versions['ICD9'] = ("9",
                        "ICD9")
    versions['ICD10'] = ("10",
                         "ICD10",
                         "ICD10-CM",
                         "ICD10-PCS")
    versions['DRG'] = ("DRG",
                       "DIAGNOSTIC RELATED GROUP",
                       "DIAGNOSTIC GROUPING",
                       "MS-DRG")
    versions['CPT4'] = ("CPT4",
                        "CPT")

    # Make a copy of the dataframe to avoid warnings about working on the original
    df = df[[patient_id, preg_id, type, version, code]].copy()

    # Check the contents of the Type column and warn user if the contents don't match the expected types
    # This doesn't constitute an error as the dataset could contain valid codes from other systems for other uses
    df[type] = df[type].str.lower()
    df_types = set(df[type].unique().flat)
    this_types = set([val for value in types.values() for val in value])
    if not df_types.issubset(this_types):
        warnings.warn(f"Some code types ({df_types - this_types}) do not match {this_types}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Check the contents of the Version column and warn user if the contents don't match the expected
    # This doesn't constitute an error as the dataset could contain valid codes from other systems for other uses
    df[version] = df[version].str.upper()
    df_versions = set(df[version].unique().flat)
    this_versions = set([val for value in versions.values() for val in value])
    if not df_versions.issubset(this_versions):
        warnings.warn(f"Some code versions ({df_versions - this_versions}) do not match {this_versions}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Convert dictionary to dataframe
    types = pd.DataFrame.from_dict(types, orient='index').stack().to_frame()
    types = pd.DataFrame(types[0].values.tolist(), index=types.index).reset_index().drop('level_1', axis=1)
    types.columns = [type, 'type_match']

    # Convert dictionary to dataframe
    versions = pd.DataFrame.from_dict(versions, orient='index').stack().to_frame()
    versions = pd.DataFrame(versions[0].values.tolist(), index=versions.index).reset_index().drop('level_1', axis=1)
    versions.columns = [version, 'version_match']

    # Replace Type and Version in the provided dataframe with standard forms
    df = df.merge(types,
                  how='inner',
                  left_on=type,
                  right_on='type_match',
                  suffixes=('_x', '')) \
        .merge(versions,
               how='inner',
               left_on=version,
               right_on='version_match',
               suffixes=('_x', '')) \
        .drop(columns=[f'{version}_x', 'version_match', f'{type}_x', 'type_match'])

    # Remove decimals from codes
    df[code] = df[code].str.replace(r'\.', '', regex=True)
    # Ensure codes are uppercase
    df[code] = df[code].str.upper()

    cesarean_encs = df.copy()
    cesarean_encs['join'] = df[code].replace(cesarean['code'].to_list(), cesarean['code'].to_list(), regex=True)
    fg_encs = df.copy()
    fg_encs['join'] = df[code].replace(fg['code'].to_list(), fg['code'].to_list(), regex=True)
    gdm_encs = df.copy()
    gdm_encs['join'] = df[code].replace(gdm['code'].to_list(), gdm['code'].to_list(), regex=True)
    ght_encs = df.copy()
    ght_encs['join'] = df[code].replace(ght['code'].to_list(), ght['code'].to_list(), regex=True)
    pe_encs = df.copy()
    pe_encs['join'] = df[code].replace(pe['code'].to_list(), pe['code'].to_list(), regex=True)

    # Get the instances of the APOs
    cesarean_encs = cesarean_encs.merge(cesarean,
                             how='inner',
                             left_on=[type, version, 'join'],
                             right_on=[type, version, code]).drop(columns=['join'])
    fg_encs = fg_encs.merge(fg,
                            how='inner',
                            left_on=[type, version, 'join'],
                            right_on=[type, version, code]).drop(columns=['join'])
    gdm_encs = gdm_encs.merge(gdm,
                              how='inner',
                              left_on=[type, version, 'join'],
                              right_on=[type, version, code]).drop(columns=['join'])
    ght_encs = ght_encs.merge(ght,
                              how='inner',
                              left_on=[type, version, 'join'],
                              right_on=[type, version, code]).drop(columns=['join'])
    pe_encs = pe_encs.merge(pe,
                            how='inner',
                            left_on=[type, version, 'join'],
                            right_on=[type, version, code]).drop(columns=['join'])

    # Limit to only the pregnancy identifiers
    cesarean_encs = cesarean_encs[[patient_id, preg_id]].drop_duplicates()
    fg_encs = fg_encs[[patient_id, preg_id]].drop_duplicates()
    gdm_encs = gdm_encs[[patient_id, preg_id]].drop_duplicates()
    ght_encs = ght_encs[[patient_id, preg_id]].drop_duplicates()
    pe_encs = pe_encs[[patient_id, preg_id]].drop_duplicates()

    # Set boolean variables
    cesarean_encs['cesarean'] = True
    fg_encs['fetal growth restriction'] = True
    gdm_encs['gest diabetes mellitus'] = True
    ght_encs['gest hypertension'] = True
    pe_encs['preeclampsia'] = True

    # Build output with APOs assigned to
    apo_out = df[[patient_id, preg_id]].drop_duplicates()
    apo_out = apo_out.merge(cesarean_encs,
                            how='left',
                            left_on=[patient_id, preg_id],
                            right_on=[patient_id, preg_id])\
        .merge(fg_encs,
               how='left',
               left_on=[patient_id, preg_id],
               right_on=[patient_id, preg_id])\
        .merge(gdm_encs,
               how='left',
               left_on=[patient_id, preg_id],
               right_on=[patient_id, preg_id])\
        .merge(ght_encs,
               how='left',
               left_on=[patient_id, preg_id],
               right_on=[patient_id, preg_id])\
        .merge(pe_encs,
               how='left',
               left_on=[patient_id, preg_id],
               right_on=[patient_id, preg_id])\
        .fillna(False)

    return apo_out
