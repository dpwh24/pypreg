"""
Process to attach the outcome map to the data.

Accepts a dataframe that contains, at a minimum, columns that hold a
diagnostic, PROCEDURE, or DRG CODE; a CODE_TYPE descriptor to define
if the CODE is diagnostic, PROCEDURE, or DRG; and VERSION information
about the CODE to indicate if the CODE is ICD9, ICD10, DRG, or CPT/HCPCS.
"""


import pandas as pd
from .outcome_map import OUTCOMES, ICD9, ICD10


def attach_map(df: pd.DataFrame,
               code_col: str,
               type_col: str,
               version_col: str,
               expanded: bool = False):
    """
    Method to attach outcome classification to diagnostic, PROCEDURE,
    and DRG codes. Moll/Crosswalk codes are used by default, user may
    expand the list by setting the EXPANDED parameter.

    :param df: pandas dataframe containing diagnostic codes and the CODE versions

    :param code_col: Column containing diagnostic codes
    :param type_col: Column containing information about the category of CODE (DX/PX/DRG)
    :param version_col: Column containing VERSION info about the CODE (ICD9/ICD10/CPT/DRG)
    :param expanded: Defaults to False, user may elect to include the EXPANDED
    CODE selection or only use the Moll/Crosswalk codes

    :return: Returns the original dataframe with the outcome classification
    """

    # cols = df.columns

    # Set reference for versions to be consistent
    versions = [ICD9,
                ICD10]

    # The regex does not consider dots, remove them
    df['adjusted_code'] = df[code_col].str.replace('.', '', regex=False)

    # Limit the OUTCOMES regex to their relevant sections to avoid erroneous matches
    dx9_outcomes, dx10_outcomes, px_outcomes, drg_outcomes = map_version_split(expanded)

    # Limit the data to be matched by code_type
    df_dx = df[df[type_col] == 'DX'].copy().drop_duplicates()
    df_px = df[df[type_col] == 'PX'].copy().drop_duplicates()
    df_drg = df[df[type_col] == 'DRG'].copy().drop_duplicates()

    # Limit the diagnoses by VERSION since these can have overlap
    df_dx9 = df_dx[df_dx[version_col] == versions[0]].copy()
    df_dx10 = df_dx[df_dx[version_col] == versions[1]].copy()

    # Apply the regex to the cleaned CODE column
    df_dx9['regex'] = df_dx9['adjusted_code'].replace(dx9_outcomes['CODE'].to_list(),
                                                      dx9_outcomes['CODE'].to_list(),
                                                      regex=True)
    df_dx10['regex'] = df_dx10['adjusted_code'].replace(dx10_outcomes['CODE'].to_list(),
                                                        dx10_outcomes['CODE'].to_list(),
                                                        regex=True)
    df_px['regex'] = df_px['adjusted_code'].replace(px_outcomes['CODE'].to_list(),
                                                    px_outcomes['CODE'].to_list(),
                                                    regex=True)
    df_drg['regex'] = df_drg['adjusted_code'].replace(drg_outcomes['CODE'].to_list(),
                                                      drg_outcomes['CODE'].to_list(),
                                                      regex=True)

    # Attach the OUTCOMES by matching on the regex string
    matched_dx9 = df_dx9.merge(dx9_outcomes[['CODE', 'outcome']],
                               how='inner',
                               left_on='regex',
                               right_on='CODE',
                               suffixes=('', '_x'))
    matched_dx10 = df_dx10.merge(dx10_outcomes[['CODE', 'outcome']],
                                 how='inner',
                                 left_on='regex',
                                 right_on='CODE',
                                 suffixes=('', '_x'))
    matched_px = df_px.merge(px_outcomes[['CODE', 'outcome']],
                             how='inner',
                             left_on='regex',
                             right_on='CODE',
                             suffixes=('', '_x'))
    matched_drg = df_drg.merge(drg_outcomes[['CODE', 'outcome']],
                               how='inner',
                               left_on='regex',
                               right_on='CODE',
                               suffixes=('', '_x'))

    # Combine the output into one dataframe
    output = pd.concat([matched_dx9, matched_dx10, matched_px, matched_drg])

    # Remove columns not needed by user
    output.drop(columns=['regex', 'code_x', 'adjusted_code'], inplace=True)
    # output.rename(columns={'outcome_y': 'outcome'}, inplace=True)
    # output.columns = output.columns.str.rstrip("_y")

    return output


def map_version_split(expanded: bool = False):
    """
    Method to split the full list of pregnancy outcome codes into 4 subtypes:
     -diagnostic codes
      -ICD-9
      -ICD-10
     -PROCEDURE codes
     -diagnostic related group codes
    :param expanded: Boolean to indicate that an EXPANDED CODE list is desired.
    Defaults to only the CODE list adapted from Moll.
    :return: Returns 4 dataframes with pregnancy endpoint codes in this order:
    ICD-9 diagnostic codes, ICD-10 diagnostic codes, PROCEDURE codes,
    diagnostic related group codes.
    """

    # Limit the map to Moll/Crosswalk by default
    map_df = OUTCOMES[OUTCOMES.schema != 'EXPANDED']

    # Reassign the full OUTCOMES list if user expands
    if expanded:
        map_df = OUTCOMES

    # Limit the OUTCOMES regex to their relevant sections to avoid erroneous matches
    dx9_outcomes = map_df[(map_df.CODE_TYPE == 'DX') & (map_df.VERSION == ICD9)]
    dx10_outcomes = map_df[(map_df.CODE_TYPE == 'DX') & (map_df.VERSION == ICD10)]
    px_outcomes = map_df[map_df.CODE_TYPE == 'PX']
    drg_outcomes = map_df[map_df.CODE_TYPE == 'DRG']

    return dx9_outcomes, dx10_outcomes, px_outcomes, drg_outcomes
