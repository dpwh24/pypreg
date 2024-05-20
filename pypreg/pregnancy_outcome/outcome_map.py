"""
Source material codes have been translated into regex and crosswalked to ICD-9 by David Walsh.
They include the top-level CODE to account for idiosyncracies in different secondary data sources.

Original codes are sourced from:
    Moll K FK Wong H-L. Task order HHSF22301001T: Pregnancy OUTCOMES
validation final report. U.S. Food; Drug Administration; 2020. Available at:
https://www.bestinitiative.org/wp-content/uploads/2020/08/Validating_
Pregnancy_Outcomes_Linked_Database_Report_2020-1.pdf

Crosswalked codes are retrieved via General Equivalence Mappings.
ICD10 codes are mapped back to ICD9, and ICD9 codes are mapped forward
to ICD10. The resulting codes were reviewed and kept if they are related
to an obstetric outcome, and if the original ICD10 CODE broadly refers
to labor and DELIVERY, then the mapped codes may also.

Expanded codes were added based upon a review of ICD9 and ICD10 codes
for other obstetric OUTCOMES not captured, specifically the delivered
episode of care codes contained in ICD9.
"""

import pandas as pd

PROCEDURE = 'PX'
DIAGNOSIS = 'DX'
ICD9 = 'ICD9'
ICD10 = 'ICD10'
CPT = 'CPT'
DRG = 'DRG'
MOLL = 'MOLL'
CROSSWALK = 'CROSSWALK'
EXPANDED = 'EXPANDED'
OUTCOME_LIST = ['LIVE_BIRTH',
                'STILLBIRTH',
                'DELIVERY',
                'TROPHOBLASTIC',
                'ECTOPIC',
                'THERAPEUTIC_ABORTION',
                'SPONTANEOUS_ABORTION']
OUTCOME_COL = 'outcome'

# ======================
# Ectopic
# ======================
ECTOPIC = dict()
ECTOPIC[DIAGNOSIS] = dict()
ECTOPIC[DIAGNOSIS][ICD10] = dict()
ECTOPIC[DIAGNOSIS][ICD10][MOLL] = (
    r"^O0[0,8].*",
)

ECTOPIC[DIAGNOSIS][ICD9] = dict()
ECTOPIC[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^633.*",
)

ECTOPIC[PROCEDURE] = dict()
ECTOPIC[PROCEDURE][ICD9] = dict()
ECTOPIC[PROCEDURE][ICD9][CROSSWALK] = (
    r"^743$",
    r"^66[0,6]2$",
)

ECTOPIC[PROCEDURE][ICD10] = dict()
ECTOPIC[PROCEDURE][ICD10][MOLL] = (
    r"^10(D2[7,8]|T2[0,3,4,7,8])ZZ$",
)

ECTOPIC[PROCEDURE][CPT] = dict()
ECTOPIC[PROCEDURE][CPT][MOLL] = (
    r"^591([0,4]0|[2,5][0,1]|3[0,5,6])$",
)

ECTOPIC[DRG] = dict()
ECTOPIC[DRG][DRG] = dict()
ECTOPIC[DRG][DRG][MOLL] = (
    r"^777$",
)

ECTOPIC[DRG][DRG][EXPANDED] = (
    r"^378$",
)

# ======================
# Trophoblastic
# ======================
TROPHOBLASTIC = dict()
TROPHOBLASTIC[DIAGNOSIS] = dict()
TROPHOBLASTIC[DIAGNOSIS][ICD10] = dict()
TROPHOBLASTIC[DIAGNOSIS][ICD10][MOLL] = (
    r"^O0(1|2([0,9]|89)).*",
)

TROPHOBLASTIC[DIAGNOSIS][ICD9] = dict()
TROPHOBLASTIC[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^63(0|18).*",
)

TROPHOBLASTIC[PROCEDURE] = dict()
TROPHOBLASTIC[PROCEDURE][CPT] = dict()
TROPHOBLASTIC[PROCEDURE][CPT][MOLL] = (
    r"^59870$",
)

# ======================
# Spontaneous Abortion
# ======================
SPONTANEOUS_ABORTION = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS] = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS][ICD10] = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS][ICD10][MOLL] = (
    r"^O0(21|3).*",
)

SPONTANEOUS_ABORTION[DIAGNOSIS][ICD9] = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^63[2,4].*",
)

SPONTANEOUS_ABORTION[PROCEDURE] = dict()
SPONTANEOUS_ABORTION[PROCEDURE][CPT] = dict()
SPONTANEOUS_ABORTION[PROCEDURE][CPT][MOLL] = (
    r"^01965$",
    r"^598(12|2[0,1]|30)$"
)

# ======================
# Elective/Therapeutic Abortion
# ======================
THERAPEUTIC_ABORTION = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS] = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS][ICD10] = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS][ICD10][MOLL] = (
    r"^O04.*",
    r"^Z332.*",
)

THERAPEUTIC_ABORTION[DIAGNOSIS][ICD9] = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^63[5-7].*",
)

THERAPEUTIC_ABORTION[PROCEDURE] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][ICD10] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][ICD10][MOLL] = (
    r"^10A0([03478]ZZ|7Z[6,W,X])$",
)

THERAPEUTIC_ABORTION[PROCEDURE][ICD9] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][ICD9][CROSSWALK] = (
    r"^7(491|50)$",
    r"^69([0,5]1|93)$"
)

THERAPEUTIC_ABORTION[PROCEDURE][CPT] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][CPT][MOLL] = (
    r"^0196[4,6]$",
    r"^598(4[0,1]|5[0-2,5-7])$",
    r"^S(0199|226[0,2,5-7])$",
)

THERAPEUTIC_ABORTION[DRG] = dict()
THERAPEUTIC_ABORTION[DRG][DRG] = dict()
THERAPEUTIC_ABORTION[DRG][DRG][MOLL] = (
    r"^77[0,9]$",
)

THERAPEUTIC_ABORTION[DRG][DRG][EXPANDED] = (
    r"^38[0,1]$",
)

# ======================
# Stillbirth
# ======================
STILLBIRTH = dict()
STILLBIRTH[DIAGNOSIS] = dict()
STILLBIRTH[DIAGNOSIS][ICD10] = dict()
STILLBIRTH[DIAGNOSIS][ICD10][MOLL] = (
    r"^Z37[1,4,7].*",
    r"^O364XX[0-5,9]$",
)

STILLBIRTH[DIAGNOSIS][ICD9] = dict()
STILLBIRTH[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^6564[013]$",
    r"^V27[1,4,7].*",
)

# ======================
# Live birth
# ======================
LIVE_BIRTH = dict()
LIVE_BIRTH[DIAGNOSIS] = dict()
LIVE_BIRTH[DIAGNOSIS][ICD10] = dict()
LIVE_BIRTH[DIAGNOSIS][ICD10][MOLL] = (
    r"^Z37([0,2,3]|[5,6][0-4,9]).*",
    r"^O80.*",
)

LIVE_BIRTH[DIAGNOSIS][ICD10][EXPANDED] = (
    r"^Z38[0,3,6].*",
)

LIVE_BIRTH[DIAGNOSIS][ICD9] = dict()
LIVE_BIRTH[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^650$",
    r"^V27[0,2,3,5,6]$",
)

LIVE_BIRTH[DIAGNOSIS][ICD9][EXPANDED] = (
    r"^V3[0-9]0.*",
)

# ======================
# Delivery of Unknown code_type
# ======================
DELIVERY = dict()
DELIVERY[DIAGNOSIS] = dict()
DELIVERY[DIAGNOSIS][ICD10] = dict()
DELIVERY[DIAGNOSIS][ICD10][MOLL] = (
    r"^Z3(79|90)$",
    r"^O420.*",
    r"^O6([3-5,7-9]|0[1,2]|6[0-3,5,6,8,9]).*",
    r"^O7([0,4,6,7]|[1,2]1|5[0,2,3,5,8,9]).*",
    r"^O8(2|8[0-3,8]2)$",
    r"^O9(8[0-9]2|9([0,1,4-7]2|2[1,8]4|3[1-5]4|8[1-4]4)|A[1-5]2).*",
)

DELIVERY[DIAGNOSIS][ICD10][EXPANDED] = (
    r"^O(151|62).*",
)

DELIVERY[DIAGNOSIS][ICD9] = dict()
DELIVERY[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^V2(40|79).*",
    r"^64(1[3,8,9]1|421|681|7[0-6,8,9]1|8[1-6,8,9]1|9([0-4]1|8)).*",
    r'^65(2[2,4,6,8,9]1|3[0-5]1|491|6[3,8]1|8[1,3]1|9([2,3,8,9][013]?|71))$',
    r"^66(0[0-5,7-9]|[2,3]|4[0-4,6]|[5,6]1|8[0-2,8,9][1,2]|9[0,5-9]).*",
    r"^67([4,9]0[1,2]|3[0-3,8][1,2]).*",
)

DELIVERY[DIAGNOSIS][ICD9][EXPANDED] = (
    r"^64(0[089]1|1[0-2]1|2[0-79][12]|3[0-289]1|5[12]1|6([0379]1|[124-6][12]|82)|"
    r"7[0-689]2|8([1-689]2|[07][12])|9([0-4]2|6[12]|[57]1)).*",
    r"^65([1,5][0-9]1|2[0,1,3,5,7]1|3[6-9]1|4([0,1,3-8][1,2]|21|92)|"
    r"6[0-2,5-7,9]1|701|8[0,2,4,8,9]1|9[0,1,4-6]1).*",
    r"^66(061|1[0-4,9]1|4[5,8,9]|5([0,3-6]1|22|[7-9][1,2])|"
    r"6(0|[2,3]2)|7[0,1]2|9([1,2,4][1,2]|32)).*",
    r"^67(0[0-3,8]2|1([0-2,5,8,9][1,2]|31|42)|202|4([1-4,8,9]2|5[1,2])|"
    r"5[0-2,8,9][1,2]|6[0-6,8,9][1,2]|8[0,1]1|91[1,2]).*",
)

DELIVERY[PROCEDURE] = dict()
DELIVERY[PROCEDURE][ICD10] = dict()
DELIVERY[PROCEDURE][ICD10][MOLL] = (
    r"^0W8NXZZ$",
    r"^10(D(0|1[7,8]Z9)|E0).*",
)

DELIVERY[PROCEDURE][ICD9] = dict()
DELIVERY[PROCEDURE][ICD9][CROSSWALK] = (
    r'^7(2[0-3,5-9][0-9]?|3(22|[5,6,9][0-9]?)|4([0-4]|99)|54)$',
)

DELIVERY[PROCEDURE][CPT] = dict()
DELIVERY[PROCEDURE][CPT][MOLL] = (
    r"^0196[0-3,7-9]$",
    r"^59(05[0,1]|4(09|1[0,4])|5(1[4,5]|25)|6(1[2,4]|2[0,2]))$",
    r"^994(36|6[4,5])$",
    r"^G9356$",
)

DELIVERY[DRG] = dict()
DELIVERY[DRG][DRG] = dict()
DELIVERY[DRG][DRG][MOLL] = (
    r"^37[0-5]$",
    r"^7(6[5-8]|7[4,5])$",
)

# ======================
# Convert to Pandas
# ======================
ECTOPIC = pd.DataFrame.from_dict(ECTOPIC, orient='index').stack().to_frame()
ECTOPIC = pd.DataFrame(ECTOPIC[0].values.tolist(),
                       index=ECTOPIC.index)
ECTOPIC = ECTOPIC.stack().to_frame()
ECTOPIC = pd.DataFrame(ECTOPIC[0].values.tolist(),
                       index=ECTOPIC.index).stack().reset_index().drop('level_3', axis=1)
ECTOPIC['outcome'] = OUTCOME_LIST[4]

TROPHOBLASTIC = pd.DataFrame.from_dict(TROPHOBLASTIC,
                                       orient='index').stack().to_frame()
TROPHOBLASTIC = pd.DataFrame(TROPHOBLASTIC[0].values.tolist(),
                             index=TROPHOBLASTIC.index)
TROPHOBLASTIC = TROPHOBLASTIC.stack().to_frame()
TROPHOBLASTIC = pd.DataFrame(TROPHOBLASTIC[0].values.tolist(),
                             index=TROPHOBLASTIC.index)\
    .stack().reset_index().drop('level_3', axis=1)
TROPHOBLASTIC['outcome'] = OUTCOME_LIST[3]

SPONTANEOUS_ABORTION = pd.DataFrame.from_dict(SPONTANEOUS_ABORTION,
                                              orient='index').stack().to_frame()
SPONTANEOUS_ABORTION = pd.DataFrame(SPONTANEOUS_ABORTION[0].values.tolist(),
                                    index=SPONTANEOUS_ABORTION.index)
SPONTANEOUS_ABORTION = SPONTANEOUS_ABORTION.stack().to_frame()
SPONTANEOUS_ABORTION = pd.DataFrame(SPONTANEOUS_ABORTION[0].values.tolist(),
                                    index=SPONTANEOUS_ABORTION.index)\
    .stack().reset_index().drop('level_3', axis=1)
SPONTANEOUS_ABORTION['outcome'] = OUTCOME_LIST[6]

THERAPEUTIC_ABORTION = pd.DataFrame.from_dict(THERAPEUTIC_ABORTION,
                                              orient='index').stack().to_frame()
THERAPEUTIC_ABORTION = pd.DataFrame(THERAPEUTIC_ABORTION[0].values.tolist(),
                                    index=THERAPEUTIC_ABORTION.index)
THERAPEUTIC_ABORTION = THERAPEUTIC_ABORTION.stack().to_frame()
THERAPEUTIC_ABORTION = pd.DataFrame(THERAPEUTIC_ABORTION[0].values.tolist(),
                                    index=THERAPEUTIC_ABORTION.index)\
    .stack().reset_index().drop('level_3', axis=1)
THERAPEUTIC_ABORTION['outcome'] = OUTCOME_LIST[5]

STILLBIRTH = pd.DataFrame.from_dict(STILLBIRTH, orient='index').stack().to_frame()
STILLBIRTH = pd.DataFrame(STILLBIRTH[0].values.tolist(),
                          index=STILLBIRTH.index)
STILLBIRTH = STILLBIRTH.stack().to_frame()
STILLBIRTH = pd.DataFrame(STILLBIRTH[0].values.tolist(),
                          index=STILLBIRTH.index).stack().reset_index().drop('level_3', axis=1)
STILLBIRTH['outcome'] = OUTCOME_LIST[1]

LIVE_BIRTH = pd.DataFrame.from_dict(LIVE_BIRTH, orient='index').stack().to_frame()
LIVE_BIRTH = pd.DataFrame(LIVE_BIRTH[0].values.tolist(),
                          index=LIVE_BIRTH.index)
LIVE_BIRTH = LIVE_BIRTH.stack().to_frame()
LIVE_BIRTH = pd.DataFrame(LIVE_BIRTH[0].values.tolist(),
                          index=LIVE_BIRTH.index).stack().reset_index().drop('level_3', axis=1)
LIVE_BIRTH['outcome'] = OUTCOME_LIST[0]

DELIVERY = pd.DataFrame.from_dict(DELIVERY, orient='index').stack().to_frame()
DELIVERY = pd.DataFrame(DELIVERY[0].values.tolist(),
                        index=DELIVERY.index)
DELIVERY = DELIVERY.stack().to_frame()
DELIVERY = pd.DataFrame(DELIVERY[0].values.tolist(),
                        index=DELIVERY.index).stack().reset_index().drop('level_3', axis=1)
DELIVERY['outcome'] = OUTCOME_LIST[2]

OUTCOMES_COLUMNS = ['code_type', 'version', 'schema', 'code', 'outcome']
ECTOPIC.columns = OUTCOMES_COLUMNS
TROPHOBLASTIC.columns = OUTCOMES_COLUMNS
SPONTANEOUS_ABORTION.columns = OUTCOMES_COLUMNS
THERAPEUTIC_ABORTION.columns = OUTCOMES_COLUMNS
STILLBIRTH.columns = OUTCOMES_COLUMNS
LIVE_BIRTH.columns = OUTCOMES_COLUMNS
DELIVERY.columns = OUTCOMES_COLUMNS

OUTCOMES = pd.concat([
    ECTOPIC,
    TROPHOBLASTIC,
    SPONTANEOUS_ABORTION,
    THERAPEUTIC_ABORTION,
    STILLBIRTH,
    LIVE_BIRTH,
    DELIVERY,
])
