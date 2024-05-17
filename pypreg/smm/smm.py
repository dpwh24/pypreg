"""
SMM Severe Maternal Morbidity

Author:
Dave Walsh 30 May 2023
Department of Biomedical and Health Informatics
UMKC

Looks at a pandas dataframe containing ICD9 and IC10 diagnostic and procedure codes to report out the presence of
Severe Maternal Morbidity (SMM) and transfusion. The function includes an option to report out the subgroups
making up an SMM determination. The function can also accept codes in other systems, but will ignore them.

Since SMM is only defined in the context of a delivery encounter, the user should ensure that they are only
processing data from delivery/outcome encounters.

SMM definition is based on the CDC definition:
https://www.cdc.gov/reproductivehealth/maternalinfanthealth/smm/severe-morbidity-ICD.htm

The codes used in the module are derived from the updated code list provided
by the Alliance for Innovation on Maternal Health:
https://saferbirth.org/aim-resources/implementation-resources/
https://saferbirth.org/wp-content/uploads/Updated-AIM-SMM-Code-List_10152021.xlsx

"""

from .smm_mapping import _smm, transfusion, icd9, icd10
import pandas as pd
import warnings


def smm(df: pd.DataFrame,
        id: str,
        type: str,
        version: str,
        code: str,
        indicators: bool = False):
    """
    Processes a pandas dataframe to indicate if an encounter contained codes consistent with
    Severe Maternal Morbidity(SMM).

    :param df: A pandas dataframe that contains at least 4 columns to identify the delivery encounter, the type of code,
    the version of the code, and the code itself - encounters may exist on multiple lines to account for multiple codes
    :param id: Encounter identifier that contains the pregnancy outcome
    :param type: Code type. One of either DX - Diagnosis or PX - Procedure
    :param version:  Only accepts code versions for ICD9 or ICD10 (9/ICD9, 10/ICD10/ICD10-CM/ICD10-PCS)
    :param code: The DX or PX code assigned during that encounter
    :param indicators: Optional boolean to return the full slate of indicators and not only SMM and Transfusion columns

    :return: Returns a condensed pandas dataframe with the delivery encounter identifier and indicators for SMM
    and transfusion.
    Optionally returned individualized indicators for each of the 20 other classes that make up SMM.

    """

    # Error checking to ensure the reported columns are contained in the dataframe
    if not {id, type, version, code}.issubset(df.columns):
        raise KeyError(f"Ensure that columns {[id, type, version, code]} are present in the data.")

    package_cols = {id: 'encounter_id',
                    version: 'version',
                    type: 'type',
                    code: 'code'
                    }
    restore_cols = {i: j for j, i in package_cols.items()}

    # Refactor the passed column names
    id = package_cols[id]
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

    # Versions can accept different coding systems: 9/ICD9, 10/ICD10/ICD10-CM/ICD10-PCS
    versions = dict()
    versions['ICD9'] = ("9",
                        "ICD9")
    versions['ICD10'] = ("10",
                         "ICD10",
                         "ICD10-CM",
                         "ICD10-PCS")

    # Make a copy of the dataframe to avoid warnings about working on the original
    df = df[[id, type, version, code]].copy()

    # Check the contents of the Type column and warn user if the contents don't match the expected types
    # This doesn't constitute an error as the dataset could contain valid codes from other systems for other uses
    df[type] = df[type].str.lower()
    df_types = set(df[type].unique().flat)
    this_types = set([val for value in types.values() for val in value])
    if not df_types.issubset(this_types):
        warnings.warn(f"Some code types ({df_types-this_types}) do not match {this_types}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Check the contents of the Version column and warn user if the contents don't match the expected
    # This doesn't constitute an error as the dataset could contain valid codes from other systems for other uses
    df[version] = df[version].str.upper()
    df_versions = set(df[version].unique().flat)
    this_versions = set([val for value in versions.values() for val in value])
    if not df_versions.issubset(this_versions):
        warnings.warn(f"Some code versions ({df_versions-this_versions}) do not match {this_versions}."
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
                  suffixes=('_x', ''))\
        .merge(versions,
               how='inner',
               left_on=version,
               right_on='version_match',
               suffixes=('_x', ''))\
        .drop(columns=[f'{version}_x', 'version_match', f'{type}_x', 'type_match'])

    # Remove decimals from codes
    df[code] = df[code].str.replace(r'\.', '', regex=True)
    # Ensure codes are uppercase
    df[code] = df[code].str.upper()

    # Limit the outcomes regex to their relevant sections to avoid erroneous matches
    dx9_smm, dx10_smm, px_smm = map_version_split()

    # Limit the data to be matched by type
    df_dx = df[df[type] == 'DX'].copy().drop_duplicates()
    df_px = df[df[type] == 'PX'].copy().drop_duplicates()
    df_transfusion = df[df[type] == 'PX'].copy().drop_duplicates()

    # Limit the diagnoses by version since these can have overlap
    df_dx9 = df_dx[df_dx[version] == icd9].copy()
    df_dx10 = df_dx[df_dx[version] == icd10].copy()

    # Apply the regex to the cleaned code column
    df_dx9['regex'] = df_dx9[code].replace(dx9_smm['smm_code'].to_list(),
                                           dx9_smm['smm_code'].to_list(),
                                           regex=True)
    df_dx10['regex'] = df_dx10[code].replace(dx10_smm['smm_code'].to_list(),
                                             dx10_smm['smm_code'].to_list(),
                                             regex=True)
    df_px['regex'] = df_px[code].replace(px_smm['smm_code'].to_list(),
                                         px_smm['smm_code'].to_list(),
                                         regex=True)
    df_transfusion['regex'] = df_transfusion[code].replace(transfusion['smm_code'].to_list(),
                                                           transfusion['smm_code'].to_list(),
                                                           regex=True)

    # Apply SMM and Transfusion indicators to the pandas df
    matched_dx9 = df_dx9.merge(dx9_smm[['smm_code', 'smm']],
                               how='inner',
                               left_on='regex',
                               right_on='smm_code',
                               suffixes=('', '_x'))
    matched_dx10 = df_dx10.merge(dx10_smm[['smm_code', 'smm']],
                                 how='inner',
                                 left_on='regex',
                                 right_on='smm_code',
                                 suffixes=('', '_x'))
    matched_px = df_px.merge(px_smm[['smm_code', 'smm']],
                             how='inner',
                             left_on='regex',
                             right_on='smm_code',
                             suffixes=('', '_x'))
    matched_transfusion = df_transfusion.merge(transfusion[['smm_code', 'transfusion']],
                                               how='inner',
                                               left_on='regex',
                                               right_on='smm_code',
                                               suffixes=('', '_x'))

    # # Apply SMM and Transfusion indicators to the pandas df
    # smm_encs = df.merge(_smm[['smm_type', 'smm_version', 'smm_code', 'smm']],
    #                     how='inner',
    #                     left_on=[type, version, code],
    #                     right_on=['smm_type', 'smm_version', 'smm_code'])\
    #     .drop_duplicates()
    # transfusion_encs = df.merge(transfusion,
    #                             how='inner',
    #                             left_on=[type, version, code],
    #                             right_on=['smm_type', 'smm_version', 'smm_code'])

    smm_encs = pd.concat([matched_dx9,
                          matched_dx10,
                          matched_px])


    # If the user wants a reporting of each indicator in addition to SMM and transfusion
    if indicators:
        # Join the SMM panda again, but keep the indicator column.
        # This may result in an indicator not being present in the final output as it's not present in the data
        matched_dx9_indicators = matched_dx9.merge(_smm[['indicator', 'smm_type', 'smm_version', 'smm_code']],
                                                   how='right',  #right merge to keep all indicator columns
                                                   left_on=[type, version, 'regex'],
                                                   right_on=['smm_type', 'smm_version', 'smm_code']).dropna()
        matched_dx10_indicators = matched_dx10.merge(_smm[['indicator', 'smm_type', 'smm_version', 'smm_code']],
                                                     how='right',  # right merge to keep all indicator columns
                                                     left_on=[type, version, 'regex'],
                                                     right_on=['smm_type', 'smm_version', 'smm_code']).dropna()
        matched_px_indicators = matched_px.merge(_smm[['indicator', 'smm_type', 'smm_version', 'smm_code']],
                                                 how='right',  # right merge to keep all indicator columns
                                                 left_on=[type, version, 'regex'],
                                                 right_on=['smm_type', 'smm_version', 'smm_code']).dropna()
        # Pivot on the indicator column to get the presence of each SMM indicator
        matched_dx9_indicators = pd.pivot(matched_dx9_indicators,
                                          index=[id, code],
                                          columns='indicator',
                                          values='smm') \
            .reset_index(names=[id, code]) \
            .drop(columns=code) \
            .fillna(False)
        matched_dx10_indicators = pd.pivot(matched_dx10_indicators,
                                           index=[id, code],
                                           columns='indicator',
                                           values='smm') \
            .reset_index(names=[id, code]) \
            .drop(columns=code) \
            .fillna(False)
        matched_px_indicators = pd.pivot(matched_px_indicators,
                                         index=[id, code],
                                         columns='indicator',
                                         values='smm') \
            .reset_index(names=[id, code]) \
            .drop(columns=code) \
            .fillna(False)

        indicators = pd.concat([matched_dx9_indicators,
                                matched_dx10_indicators,
                                matched_px_indicators]).fillna(False)
        # Aggregate the rows down to one
        indicators = indicators.groupby(id).agg(lambda x: any(x))

        # Ensure all indicators are present
        indicator_list = _smm.indicator.drop_duplicates().to_list()
        col_list = list(set().union(indicators.columns, indicator_list))
        indicators = indicators.reindex(columns=col_list, fill_value=False)

        # Join the indicator data back to the SMM data
        smm_encs = smm_encs.merge(indicators,
                                  how='inner',
                                  left_on=id,
                                  right_index=True)
        smm_encs.index.name = None
    # Prep the output data
    warnings.simplefilter('ignore', category=FutureWarning)
    output_df = smm_encs.merge(matched_transfusion[[id, 'transfusion']],
                               how='outer',
                               left_on=id,
                               right_on=id)
    warnings.simplefilter('always')
    output_df.fillna(False, inplace=True)
    output_df.drop(columns=[code, version, type, 'smm_code', 'regex'], inplace=True)
    output_df.drop_duplicates(inplace=True)

    output_df.rename(columns=restore_cols, inplace=True)

    return output_df


def map_version_split():
    """
    Splits the map into separate components like ICD9 Dx, ICD10 DX, and PX

    :return: 3 dataframes for dx9, dx10, and px SMM codes
    """

    # Rename map reference
    map_df = _smm

    # Limit the outcomes regex to their relevant sections to avoid erroneous matches
    dx9_smm = map_df[(map_df.smm_type == 'DX') & (map_df.smm_version == icd9)]
    dx10_smm = map_df[(map_df.smm_type == 'DX') & (map_df.smm_version == icd10)]
    px_smm = map_df[map_df.smm_type == 'PX']

    return dx9_smm, dx10_smm, px_smm
