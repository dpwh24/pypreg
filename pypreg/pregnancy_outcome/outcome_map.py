"""
Source material codes have been translated into regex and crosswalked to ICD-9 by David Walsh.
They include the top-level CODE to account for idiosyncracies in different secondary data sources.

Original codes are sourced from:
    Moll K FK Wong H-L. Task order HHSF22301001T: Pregnancy outcomes
validation final report. U.S. Food; Drug Administration; 2020. Available at:
https://www.bestinitiative.org/wp-content/uploads/2020/08/Validating_
Pregnancy_Outcomes_Linked_Database_Report_2020-1.pdf

Crosswalked codes are retrieved via General Equivalence Mappings. ICD10 codes are mapped back to ICD9, and ICD9 codes
are mapped forward to ICD10. The resulting codes were reviewed and kept if they are related to an obstetric outcome, and,
if the original ICD10 CODE broadly refers to labor and delivery, then the mapped codes may also.

Expanded codes were added based upon a review of ICD9 and ICD10 codes for other obstetric outcomes not captured,
specifically the delivered episode of care codes contained in ICD9.
"""

import pandas as pd

procedure = 'PX'
diagnosis = 'DX'
icd9 = 'ICD9'
icd10 = 'ICD10'
cpt = 'CPT'
drg = 'DRG'
moll = 'moll'
crosswalk = 'crosswalk'
expanded = 'expanded'
outcome_list = ['live_birth',
                'stillbirth',
                'delivery',
                'trophoblastic',
                'ectopic',
                'therapeutic_abortion',
                'spontaneous_abortion']
outcome_col = 'outcome'

# ======================
# Ectopic
# ======================
ectopic = dict()
ectopic[diagnosis] = dict()
ectopic[diagnosis][icd10] = dict()
ectopic[diagnosis][icd10][moll] = (
    r"^O0[0,8].*",
)

ectopic[diagnosis][icd9] = dict()
ectopic[diagnosis][icd9][crosswalk] = (
    r"^633.*",
)

ectopic[procedure] = dict()
ectopic[procedure][icd9] = dict()
ectopic[procedure][icd9][crosswalk] = (
    r"^743$",
    r"^66[0,6]2$",
)

ectopic[procedure][icd10] = dict()
ectopic[procedure][icd10][moll] = (
    r"^10(D2[7,8]|T2[0,3,4,7,8])ZZ$",
)

ectopic[procedure][cpt] = dict()
ectopic[procedure][cpt][moll] = (
    r"^591([0,4]0|[2,5][0,1]|3[0,5,6])$",
)

ectopic[drg] = dict()
ectopic[drg][drg] = dict()
ectopic[drg][drg][moll] = (
    r"^777$",
)

ectopic[drg][drg][expanded] = (
    r"^378$",
)

# ======================
# Trophoblastic
# ======================
trophoblastic = dict()
trophoblastic[diagnosis] = dict()
trophoblastic[diagnosis][icd10] = dict()
trophoblastic[diagnosis][icd10][moll] = (
    r"^O0(1|2([0,9]|89)).*",
)

trophoblastic[diagnosis][icd9] = dict()
trophoblastic[diagnosis][icd9][crosswalk] = (
    r"^63(0|18).*",
)

trophoblastic[procedure] = dict()
trophoblastic[procedure][cpt] = dict()
trophoblastic[procedure][cpt][moll] = (
    r"^59870$",
)

# ======================
# Spontaneous Abortion
# ======================
spontaneous_abortion = dict()
spontaneous_abortion[diagnosis] = dict()
spontaneous_abortion[diagnosis][icd10] = dict()
spontaneous_abortion[diagnosis][icd10][moll] = (
    r"^O0(21|3).*",
)

spontaneous_abortion[diagnosis][icd9] = dict()
spontaneous_abortion[diagnosis][icd9][crosswalk] = (
    r"^63[2,4].*",
)

spontaneous_abortion[procedure] = dict()
spontaneous_abortion[procedure][cpt] = dict()
spontaneous_abortion[procedure][cpt][moll] = (
    r"^01965$",
    r"^598(12|2[0,1]|30)$"
)

# ======================
# Elective/Therapeutic Abortion
# ======================
therapeutic_abortion = dict()
therapeutic_abortion[diagnosis] = dict()
therapeutic_abortion[diagnosis][icd10] = dict()
therapeutic_abortion[diagnosis][icd10][moll] = (
    r"^O04.*",
    r"^Z332.*",
)

therapeutic_abortion[diagnosis][icd9] = dict()
therapeutic_abortion[diagnosis][icd9][crosswalk] = (
    r"^63[5-7].*",
)

therapeutic_abortion[procedure] = dict()
therapeutic_abortion[procedure][icd10] = dict()
therapeutic_abortion[procedure][icd10][moll] = (
    r"^10A0([03478]ZZ|7Z[6,W,X])$",
)

therapeutic_abortion[procedure][icd9] = dict()
therapeutic_abortion[procedure][icd9][crosswalk] = (
    r"^7(491|50)$",
    r"^69([0,5]1|93)$"
)

therapeutic_abortion[procedure][cpt] = dict()
therapeutic_abortion[procedure][cpt][moll] = (
    r"^0196[4,6]$",
    r"^598(4[0,1]|5[0-2,5-7])$",
    r"^S(0199|226[0,2,5-7])$",
)

therapeutic_abortion[drg] = dict()
therapeutic_abortion[drg][drg] = dict()
therapeutic_abortion[drg][drg][moll] = (
    r"^77[0,9]$",
)

therapeutic_abortion[drg][drg][expanded] = (
    r"^38[0,1]$",
)

# ======================
# Stillbirth
# ======================
stillbirth = dict()
stillbirth[diagnosis] = dict()
stillbirth[diagnosis][icd10] = dict()
stillbirth[diagnosis][icd10][moll] = (
    r"^Z37[1,4,7].*",
    r"^O364XX[0-5,9]$",
)

stillbirth[diagnosis][icd9] = dict()
stillbirth[diagnosis][icd9][crosswalk] = (
    r"^6564[013]$",
    r"^V27[1,4,7].*",
)

# ======================
# Live birth
# ======================
live_birth = dict()
live_birth[diagnosis] = dict()
live_birth[diagnosis][icd10] = dict()
live_birth[diagnosis][icd10][moll] = (
    r"^Z37([0,2,3]|[5,6][0-4,9]).*",
    r"^O80.*",
)

live_birth[diagnosis][icd10][expanded] = (
    r"^Z38[0,3,6].*",
)

live_birth[diagnosis][icd9] = dict()
live_birth[diagnosis][icd9][crosswalk] = (
    r"^650$",
    r"^V27[0,2,3,5,6]$",
)

live_birth[diagnosis][icd9][expanded] = (
    r"^V3[0-9]0.*",
)

# ======================
# Delivery of Unknown code_type
# ======================
delivery = dict()
delivery[diagnosis] = dict()
delivery[diagnosis][icd10] = dict()
delivery[diagnosis][icd10][moll] = (
    r"^Z3(79|90)$",
    r"^O420.*",
    r"^O6([3-5,7-9]|0[1,2]|6[0-3,5,6,8,9]).*",
    r"^O7([0,4,6,7]|[1,2]1|5[0,2,3,5,8,9]).*",
    r"^O8(2|8[0-3,8]2)$",
    r"^O9(8[0-9]2|9([0,1,4-7]2|2[1,8]4|3[1-5]4|8[1-4]4)|A[1-5]2).*",
)

delivery[diagnosis][icd10][expanded] = (
    r"^O(151|62).*",
)

delivery[diagnosis][icd9] = dict()
delivery[diagnosis][icd9][crosswalk] = (
    r"^V2(40|79).*",
    r"^64(1[3,8,9]1|421|681|7[0-6,8,9]1|8[1-6,8,9]1|9([0-4]1|8)).*",
    r'^65(2[2,4,6,8,9]1|3[0-5]1|491|6[3,8]1|8[1,3]1|9([2,3,8,9][013]?|71))$',
    r"^66(0[0-5,7-9]|[2,3]|4[0-4,6]|[5,6]1|8[0-2,8,9][1,2]|9[0,5-9]).*",
    r"^67([4,9]0[1,2]|3[0-3,8][1,2]).*",
)

delivery[diagnosis][icd9][expanded] = (
    r"^64(0[089]1|1[0-2]1|2[0-79][12]|3[0-289]1|5[12]1|6([0379]1|[124-6][12]|82)|7[0-689]2|8([1-689]2|[07][12])|9([0-4]2|6[12]|[57]1)).*",
    r"^65([1,5][0-9]1|2[0,1,3,5,7]1|3[6-9]1|4([0,1,3-8][1,2]|21|92)|6[0-2,5-7,9]1|701|8[0,2,4,8,9]1|9[0,1,4-6]1).*",
    r"^66(061|1[0-4,9]1|4[5,8,9]|5([0,3-6]1|22|[7-9][1,2])|6(0|[2,3]2)|7[0,1]2|9([1,2,4][1,2]|32)).*",
    r"^67(0[0-3,8]2|1([0-2,5,8,9][1,2]|31|42)|202|4([1-4,8,9]2|5[1,2])|5[0-2,8,9][1,2]|6[0-6,8,9][1,2]|8[0,1]1|91[1,2]).*",
)

delivery[procedure] = dict()
delivery[procedure][icd10] = dict()
delivery[procedure][icd10][moll] = (
    r"^0W8NXZZ$",
    r"^10(D(0|1[7,8]Z9)|E0).*",
)

delivery[procedure][icd9] = dict()
delivery[procedure][icd9][crosswalk] = (
    r'^7(2[0-3,5-9][0-9]?|3(22|[5,6,9][0-9]?)|4([0-4]|99)|54)$',
)

delivery[procedure][cpt] = dict()
delivery[procedure][cpt][moll] = (
    r"^0196[0-3,7-9]$",
    r"^59(05[0,1]|4(09|1[0,4])|5(1[4,5]|25)|6(1[2,4]|2[0,2]))$",
    r"^994(36|6[4,5])$",
    r"^G9356$",
)

delivery[drg] = dict()
delivery[drg][drg] = dict()
delivery[drg][drg][moll] = (
    r"^37[0-5]$",
    r"^7(6[5-8]|7[4,5])$",
)

# ======================
# Convert to Pandas
# ======================
ectopic = pd.DataFrame.from_dict(ectopic, orient='index').stack().to_frame()
ectopic = pd.DataFrame(ectopic[0].values.tolist(),
                       index=ectopic.index)
ectopic = ectopic.stack().to_frame()
ectopic = pd.DataFrame(ectopic[0].values.tolist(),
                       index=ectopic.index).stack().reset_index().drop('level_3', axis=1)
ectopic['outcome'] = outcome_list[4]

trophoblastic = pd.DataFrame.from_dict(trophoblastic, orient='index').stack().to_frame()
trophoblastic = pd.DataFrame(trophoblastic[0].values.tolist(),
                             index=trophoblastic.index)
trophoblastic = trophoblastic.stack().to_frame()
trophoblastic = pd.DataFrame(trophoblastic[0].values.tolist(),
                             index=trophoblastic.index).stack().reset_index().drop('level_3', axis=1)
trophoblastic['outcome'] = outcome_list[3]

spontaneous_abortion = pd.DataFrame.from_dict(spontaneous_abortion, orient='index').stack().to_frame()
spontaneous_abortion = pd.DataFrame(spontaneous_abortion[0].values.tolist(),
                                    index=spontaneous_abortion.index)
spontaneous_abortion = spontaneous_abortion.stack().to_frame()
spontaneous_abortion = pd.DataFrame(spontaneous_abortion[0].values.tolist(),
                                    index=spontaneous_abortion.index).stack().reset_index().drop('level_3', axis=1)
spontaneous_abortion['outcome'] = outcome_list[6]

therapeutic_abortion = pd.DataFrame.from_dict(therapeutic_abortion, orient='index').stack().to_frame()
therapeutic_abortion = pd.DataFrame(therapeutic_abortion[0].values.tolist(),
                                    index=therapeutic_abortion.index)
therapeutic_abortion = therapeutic_abortion.stack().to_frame()
therapeutic_abortion = pd.DataFrame(therapeutic_abortion[0].values.tolist(),
                                    index=therapeutic_abortion.index).stack().reset_index().drop('level_3', axis=1)
therapeutic_abortion['outcome'] = outcome_list[5]

stillbirth = pd.DataFrame.from_dict(stillbirth, orient='index').stack().to_frame()
stillbirth = pd.DataFrame(stillbirth[0].values.tolist(),
                          index=stillbirth.index)
stillbirth = stillbirth.stack().to_frame()
stillbirth = pd.DataFrame(stillbirth[0].values.tolist(),
                          index=stillbirth.index).stack().reset_index().drop('level_3', axis=1)
stillbirth['outcome'] = outcome_list[1]

live_birth = pd.DataFrame.from_dict(live_birth, orient='index').stack().to_frame()
live_birth = pd.DataFrame(live_birth[0].values.tolist(),
                          index=live_birth.index)
live_birth = live_birth.stack().to_frame()
live_birth = pd.DataFrame(live_birth[0].values.tolist(),
                          index=live_birth.index).stack().reset_index().drop('level_3', axis=1)
live_birth['outcome'] = outcome_list[0]

delivery = pd.DataFrame.from_dict(delivery, orient='index').stack().to_frame()
delivery = pd.DataFrame(delivery[0].values.tolist(),
                        index=delivery.index)
delivery = delivery.stack().to_frame()
delivery = pd.DataFrame(delivery[0].values.tolist(),
                        index=delivery.index).stack().reset_index().drop('level_3', axis=1)
delivery['outcome'] = outcome_list[2]

columns = ['code_type', 'VERSION', 'schema', 'CODE', 'outcome']
ectopic.columns = columns
trophoblastic.columns = columns
spontaneous_abortion.columns = columns
therapeutic_abortion.columns = columns
stillbirth.columns = columns
live_birth.columns = columns
delivery.columns = columns

outcomes = pd.concat([
    ectopic,
    trophoblastic,
    spontaneous_abortion,
    therapeutic_abortion,
    stillbirth,
    live_birth,
    delivery,
])
