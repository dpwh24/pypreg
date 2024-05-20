"""
Update 03Jan2024
Codes in FAD SAS CODE do not appear to be current with CDC nor HCUP definitions.
Codes were instead harmonized with CDC definition per:
    https://www.cdc.gov/reproductivehealth/maternalinfanthealth/smm/severe-morbidity-ICD.htm

Update 02Jan2024
Codes adjusted to be consistent with Federally Available Data Resource Document
Maternal and Child Health Bureau. Federally Available Data (FAD)
    Resource Document. July 18, 2023; Rockville, MD: Health Resources and
    Services Administration. Available at:
    https://mchb.tvisdata.hrsa.gov/Home/Resources

Codes sourced from Alliance for Innovation on Maternal Health Code List v12-01-2022
Codes with wildcards in the source material include the top level codes here to account for
idiosyncracies in different secondary data sources.

ICD9 codes from:
Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK An Expanded Obstetric Comorbidity
    Scoring System for Predicting Severe Maternal Morbidity. 2020-08. Obstetrics & Gynecology,
    Vol. 136, No. 3 Ovid Technologies (Wolters Kluwer Health) p. 440-449

"""


import pandas as pd

ICD9 = 'ICD9'
ICD10 = 'ICD10'

# ======================
# Acute Myocardial Infarction
# ======================
ACUTE_MI = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

ACUTE_MI[CODE_TYPE] = dict()
ACUTE_MI[CODE_TYPE][VERSION] = dict()
ACUTE_MI[CODE_TYPE][VERSION][CODE] = (
    r"^410.*",
)

VERSION = ICD10
ACUTE_MI[CODE_TYPE][VERSION] = dict()
ACUTE_MI[CODE_TYPE][VERSION][CODE] = (
    r"^I21.*",
    r"^I22.*",
)

# ======================
# Aneurysm
# ======================
ANEUR = dict()

VERSION = ICD9

ANEUR[CODE_TYPE] = dict()
ANEUR[CODE_TYPE][VERSION] = dict()
ANEUR[CODE_TYPE][VERSION][CODE] = (
    "^441.*",
)

VERSION = ICD10
ANEUR[CODE_TYPE][VERSION] = dict()
ANEUR[CODE_TYPE][VERSION][CODE] = (
    r"^I71.*",
    r"^I790$",
)

# ======================
# Acute Renal Failure
# ======================
RENAL = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

RENAL[CODE_TYPE] = dict()
RENAL[CODE_TYPE][VERSION] = dict()
RENAL[CODE_TYPE][VERSION][CODE] = (
    r"^584[5-9]$",
    r"^6693.*",
)

VERSION = ICD10
RENAL[CODE_TYPE][VERSION] = dict()
RENAL[CODE_TYPE][VERSION][CODE] = (
    "^N17.*",
    "^O904$",
)

# ======================
# Adult Respiratory Distress Syndrome
# ======================
ADULT_RDS = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

ADULT_RDS[CODE_TYPE] = dict()
ADULT_RDS[CODE_TYPE][VERSION] = dict()
ADULT_RDS[CODE_TYPE][VERSION][CODE] = (
    r"^5185.*",
    r"^5188[124]$",
    r"^7991$",
)

VERSION = ICD10
ADULT_RDS[CODE_TYPE][VERSION] = dict()
ADULT_RDS[CODE_TYPE][VERSION][CODE] = (
    r"^J80$",
    r"^J95([1-3]$|82.*)",
    r"^J96[029].*",
    r"^R0(603|92)$",
)

# ======================
# Amniotic fluid EMBOLISM
# ======================
AMNIOTIC_EMB = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

AMNIOTIC_EMB[CODE_TYPE] = dict()
AMNIOTIC_EMB[CODE_TYPE][VERSION] = dict()
AMNIOTIC_EMB[CODE_TYPE][VERSION][CODE] = (
    r"^6731.*",
)

VERSION = ICD10
AMNIOTIC_EMB[CODE_TYPE][VERSION] = dict()
AMNIOTIC_EMB[CODE_TYPE][VERSION][CODE] = (
    r"^O881(1[239]|[23])$",
)

# ======================
# Cardiac arrest/ventricular fibrilation
# ======================
CARD_ARREST = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

CARD_ARREST[CODE_TYPE] = dict()
CARD_ARREST[CODE_TYPE][VERSION] = dict()
CARD_ARREST[CODE_TYPE][VERSION][CODE] = (
    r"^427(4[12]|5)$",
)

VERSION = ICD10
CARD_ARREST[CODE_TYPE][VERSION] = dict()
CARD_ARREST[CODE_TYPE][VERSION][CODE] = (
    r"^I46.*",
    r"^I490.*",
)

# ======================
# Conversion of cardiac rhythm
# ======================
CARDIAC_RHYTHM = dict()

CODE_TYPE = 'PX'
VERSION = ICD9
CODE = 'CODE'

CARDIAC_RHYTHM[CODE_TYPE] = dict()
CARDIAC_RHYTHM[CODE_TYPE][VERSION] = dict()
CARDIAC_RHYTHM[CODE_TYPE][VERSION][CODE] = (
    r"^996.*",
)

VERSION = ICD10
CARDIAC_RHYTHM[CODE_TYPE][VERSION] = dict()
CARDIAC_RHYTHM[CODE_TYPE][VERSION][CODE] = (
    r"^5A2204Z$",
    r"^5A12012$",
)

# ======================
# Disseminated intravascular coagulation
# ======================
INTRA_COAG = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

INTRA_COAG[CODE_TYPE] = dict()
INTRA_COAG[CODE_TYPE][VERSION] = dict()
INTRA_COAG[CODE_TYPE][VERSION][CODE] = (
    r"^286[69]$",
    r"^6413.*",
    r"^6663.*",
)

VERSION = ICD10
INTRA_COAG[CODE_TYPE][VERSION] = dict()
INTRA_COAG[CODE_TYPE][VERSION][CODE] = (
    r"^D6(5|8[89])$",
    r"^O4[56]0[0-29][239]$",
    r"^O670$",
    r"^O723$",
)

# ======================
# Eclampsia
# ======================
ECLAMPSIA = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

ECLAMPSIA[CODE_TYPE] = dict()
ECLAMPSIA[CODE_TYPE][VERSION] = dict()
ECLAMPSIA[CODE_TYPE][VERSION][CODE] = (
    r"^6426.*",
)

VERSION = ICD10
ECLAMPSIA[CODE_TYPE][VERSION] = dict()
ECLAMPSIA[CODE_TYPE][VERSION][CODE] = (
    r"^O15.*",
)

# ======================
# Heart failure / arrest during surgery or procedure
# ======================
HEART_FAIL = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

HEART_FAIL[CODE_TYPE] = dict()
HEART_FAIL[CODE_TYPE][VERSION] = dict()
HEART_FAIL[CODE_TYPE][VERSION][CODE] = (
    r"^9971$",
)

VERSION = ICD10
HEART_FAIL[CODE_TYPE][VERSION] = dict()
HEART_FAIL[CODE_TYPE][VERSION][CODE] = (
    r"^I97(1[23]|71)[01]$",
)

# ======================
# Puerperal cerebrovascular disorders
# ======================
PUERP_CV = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

PUERP_CV[CODE_TYPE] = dict()
PUERP_CV[CODE_TYPE][VERSION] = dict()
PUERP_CV[CODE_TYPE][VERSION][CODE] = (
    r"^0463$",
    r"^34839$",
    r"^36234$",
    r"^43[0-7].*",
    r"^67(15|40).*",
    r"^99702$",
)

VERSION = ICD10
PUERP_CV[CODE_TYPE][VERSION] = dict()
PUERP_CV[CODE_TYPE][VERSION][CODE] = (
    r"^A812$",
    r"^G4[56].*",
    r"^G9349$",
    r"^H340.*",
    r"^I6([0-25-8].*|3(00$|01.*|[1-689].*))",
    r"^O225[023]$",
    r"^I978[12][01]$",
    r"^O873$",
)

# ======================
# Pulmonary edema / Acute heart failure
# ======================
PULM_EDEMA = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

PULM_EDEMA[CODE_TYPE] = dict()
PULM_EDEMA[CODE_TYPE][VERSION] = dict()
PULM_EDEMA[CODE_TYPE][VERSION][CODE] = (
    r"^5184$",
    r"^428([01]|[2-4][013]|9)$",
)

VERSION = ICD10
PULM_EDEMA[CODE_TYPE][VERSION] = dict()
PULM_EDEMA[CODE_TYPE][VERSION][CODE] = (
    r"^J810$",
    r"^I50([19]|[2-4][013]|81[0134]|8[2-49])$",
)

# ======================
# Severe anesthesia complications
# ======================
ANEST_COMP = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

ANEST_COMP[CODE_TYPE] = dict()
ANEST_COMP[CODE_TYPE][VERSION] = dict()
ANEST_COMP[CODE_TYPE][VERSION][CODE] = (
    r"^668[0-2].*",
    r"^995(4|86)$",
)

VERSION = ICD10
ANEST_COMP[CODE_TYPE][VERSION] = dict()
ANEST_COMP[CODE_TYPE][VERSION][CODE] = (
    r"^O29(1[129]|2[19])[239]$",
    r"^O74[0-3]$",
    r"^O89(0.*|[12]$)",
    r"^T88[23]XXA$",
)

# ======================
# Sepsis
# ======================
SEPSIS = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

SEPSIS[CODE_TYPE] = dict()
SEPSIS[CODE_TYPE][VERSION] = dict()
SEPSIS[CODE_TYPE][VERSION][CODE] = (
    r"^038.*",
    r"^6702.*",
    r"^99802$",
    r"^9959[12]$",
    r"^78552$",
    r"^449$",
)

VERSION = ICD10
SEPSIS[CODE_TYPE][VERSION] = dict()
SEPSIS[CODE_TYPE][VERSION][CODE] = (
    r"^O85$",
    r"^R652[01]$",
    r"^O8604$",
    r"^T81(12|44)XA$",
    r"^I76$",
    r"^A4[01].*",
    r"^A327$",
)

# ======================
# Shock
# ======================
SHOCK = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

SHOCK[CODE_TYPE] = dict()
SHOCK[CODE_TYPE][VERSION] = dict()
SHOCK[CODE_TYPE][VERSION][CODE] = (
    r"^6691.*",
    r"^7855[019]$",
    r"^99(50|80[019]?)$",
)

VERSION = ICD10
SHOCK[CODE_TYPE][VERSION] = dict()
SHOCK[CODE_TYPE][VERSION][CODE] = (
    r"^O751$",
    r"^R57.*",
    r"^T(782X|886X|811[019])XA$",
)

# ======================
# Sickle cell disease with crisis
# ======================
SICKLE_CELL = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

SICKLE_CELL[CODE_TYPE] = dict()
SICKLE_CELL[CODE_TYPE][VERSION] = dict()
SICKLE_CELL[CODE_TYPE][VERSION][CODE] = (
    r"^282(42|6[249])$",
    r"^28952$",
)

VERSION = ICD10
SICKLE_CELL[CODE_TYPE][VERSION] = dict()
SICKLE_CELL[CODE_TYPE][VERSION][CODE] = (
    r"^D57(0[0-2]|[248]1[129])$",
)

# ======================
# Air and thrombotic EMBOLISM
# ======================
EMBOLISM = dict()

CODE_TYPE = 'DX'
VERSION = ICD9
CODE = 'CODE'

EMBOLISM[CODE_TYPE] = dict()
EMBOLISM[CODE_TYPE][VERSION] = dict()
EMBOLISM[CODE_TYPE][VERSION][CODE] = (
    r"^415(0$|1.*)",
    r"^673[0238].*",
)

VERSION = ICD10
EMBOLISM[CODE_TYPE][VERSION] = dict()
EMBOLISM[CODE_TYPE][VERSION][CODE] = (
    r"^I26.*",
    r"^O88[0238](1[239]|[23])$",
    r"^T800XXA$",
)

# ======================
# Hysterectomy
# ======================
HYSTERECTOMY = dict()

CODE_TYPE = 'PX'
VERSION = ICD9
CODE = 'CODE'

# Removing the top level codes consistent with AIM codesheet removes 63 occurences from HF data
HYSTERECTOMY[CODE_TYPE] = dict()
HYSTERECTOMY[CODE_TYPE][VERSION] = dict()
HYSTERECTOMY[CODE_TYPE][VERSION][CODE] = (
    "^68([3-7]9?|9)$",
)

VERSION = ICD10
HYSTERECTOMY[CODE_TYPE][VERSION] = dict()
HYSTERECTOMY[CODE_TYPE][VERSION][CODE] = (
    r"^0UT9[07]Z[LZ]$",
)

# ======================
# Temporary tracheostomy
# ======================
TRACH = dict()

CODE_TYPE = 'PX'
VERSION = ICD9
CODE = 'CODE'

TRACH[CODE_TYPE] = dict()
TRACH[CODE_TYPE][VERSION] = dict()
TRACH[CODE_TYPE][VERSION][CODE] = (
    r"^311$",
)

VERSION = ICD10
TRACH[CODE_TYPE][VERSION] = dict()
TRACH[CODE_TYPE][VERSION][CODE] = (
    r"^0B11[034]F4$",
)

# ======================
# Ventilation
# ======================
VENT = dict()

CODE_TYPE = 'PX'
VERSION = ICD9
CODE = 'CODE'

VENT[CODE_TYPE] = dict()
VENT[CODE_TYPE][VERSION] = dict()
VENT[CODE_TYPE][VERSION][CODE] = (
    r"^967[0-2]$",
)

VERSION = ICD10
VENT[CODE_TYPE][VERSION] = dict()
VENT[CODE_TYPE][VERSION][CODE] = (
    r"^5A19[3-5]5Z$",
)

# ======================
# Transfusion
# ======================
TRANSFUSION = dict()

CODE_TYPE = 'PX'
VERSION = ICD9
CODE = 'CODE'

TRANSFUSION[CODE_TYPE] = dict()
TRANSFUSION[CODE_TYPE][VERSION] = dict()
TRANSFUSION[CODE_TYPE][VERSION][CODE] = (
    r"^990.*",
)

VERSION = ICD10
TRANSFUSION[CODE_TYPE][VERSION] = dict()
TRANSFUSION[CODE_TYPE][VERSION][CODE] = (
    r"^302[34][03][HK-NPRT][01]$",
)

# ======================
# Convert to Pandas
# ======================
ACUTE_MI = pd.DataFrame.from_dict(ACUTE_MI, orient='index').stack().to_frame()
ACUTE_MI = pd.DataFrame(ACUTE_MI[0].values.tolist(),
                        index=ACUTE_MI.index)
ACUTE_MI = pd.DataFrame(ACUTE_MI[CODE].values.tolist(),
                        index=ACUTE_MI.index).stack().reset_index().drop('level_2', axis=1)
ACUTE_MI['indicator'] = 'acute_myocardial_infarction'

ANEUR = pd.DataFrame.from_dict(ANEUR, orient='index').stack().to_frame()
ANEUR = pd.DataFrame(ANEUR[0].values.tolist(),
                     index=ANEUR.index)
ANEUR = pd.DataFrame(ANEUR[CODE].values.tolist(),
                     index=ANEUR.index).stack().reset_index().drop('level_2', axis=1)
ANEUR['indicator'] = 'aneurysm'

RENAL = pd.DataFrame.from_dict(RENAL, orient='index').stack().to_frame()
RENAL = pd.DataFrame(RENAL[0].values.tolist(),
                     index=RENAL.index)
RENAL = pd.DataFrame(RENAL[CODE].values.tolist(),
                     index=RENAL.index).stack().reset_index().drop('level_2', axis=1)
RENAL['indicator'] = 'acute_renal_failure'

ADULT_RDS = pd.DataFrame.from_dict(ADULT_RDS, orient='index').stack().to_frame()
ADULT_RDS = pd.DataFrame(ADULT_RDS[0].values.tolist(),
                         index=ADULT_RDS.index)
ADULT_RDS = pd.DataFrame(ADULT_RDS[CODE].values.tolist(),
                         index=ADULT_RDS.index).stack().reset_index().drop('level_2', axis=1)
ADULT_RDS['indicator'] = 'adult_respiratory_distress_syndrome'

AMNIOTIC_EMB = pd.DataFrame.from_dict(AMNIOTIC_EMB, orient='index').stack().to_frame()
AMNIOTIC_EMB = pd.DataFrame(AMNIOTIC_EMB[0].values.tolist(),
                            index=AMNIOTIC_EMB.index)
AMNIOTIC_EMB = pd.DataFrame(AMNIOTIC_EMB[CODE].values.tolist(),
                            index=AMNIOTIC_EMB.index).stack().reset_index().drop('level_2', axis=1)
AMNIOTIC_EMB['indicator'] = 'amniotic_fluid_embolism'

CARD_ARREST = pd.DataFrame.from_dict(CARD_ARREST, orient='index').stack().to_frame()
CARD_ARREST = pd.DataFrame(CARD_ARREST[0].values.tolist(),
                           index=CARD_ARREST.index)
CARD_ARREST = pd.DataFrame(CARD_ARREST[CODE].values.tolist(),
                           index=CARD_ARREST.index).stack().reset_index().drop('level_2', axis=1)
CARD_ARREST['indicator'] = 'cardiac_arrest_ventricular_fibrillation'

CARDIAC_RHYTHM = pd.DataFrame.from_dict(CARDIAC_RHYTHM, orient='index').stack().to_frame()
CARDIAC_RHYTHM = pd.DataFrame(CARDIAC_RHYTHM[0].values.tolist(),
                              index=CARDIAC_RHYTHM.index)
CARDIAC_RHYTHM = pd.DataFrame(CARDIAC_RHYTHM[CODE].values.tolist(),
                              index=CARDIAC_RHYTHM.index).stack().reset_index().drop('level_2',
                                                                                     axis=1)
CARDIAC_RHYTHM['indicator'] = 'conversion_of_cardiac_rhythm'

INTRA_COAG = pd.DataFrame.from_dict(INTRA_COAG, orient='index').stack().to_frame()
INTRA_COAG = pd.DataFrame(INTRA_COAG[0].values.tolist(),
                          index=INTRA_COAG.index)
INTRA_COAG = pd.DataFrame(INTRA_COAG[CODE].values.tolist(),
                          index=INTRA_COAG.index).stack().reset_index().drop('level_2', axis=1)
INTRA_COAG['indicator'] = 'disseminated_intravascular_coagulation'

ECLAMPSIA = pd.DataFrame.from_dict(ECLAMPSIA, orient='index').stack().to_frame()
ECLAMPSIA = pd.DataFrame(ECLAMPSIA[0].values.tolist(),
                         index=ECLAMPSIA.index)
ECLAMPSIA = pd.DataFrame(ECLAMPSIA[CODE].values.tolist(),
                         index=ECLAMPSIA.index).stack().reset_index().drop('level_2', axis=1)
ECLAMPSIA['indicator'] = 'ECLAMPSIA'

HEART_FAIL = pd.DataFrame.from_dict(HEART_FAIL, orient='index').stack().to_frame()
HEART_FAIL = pd.DataFrame(HEART_FAIL[0].values.tolist(),
                          index=HEART_FAIL.index)
HEART_FAIL = pd.DataFrame(HEART_FAIL[CODE].values.tolist(),
                          index=HEART_FAIL.index).stack().reset_index().drop('level_2', axis=1)
HEART_FAIL['indicator'] = 'heart_failure_arrest_during_surgery_or_procedure'

PUERP_CV = pd.DataFrame.from_dict(PUERP_CV, orient='index').stack().to_frame()
PUERP_CV = pd.DataFrame(PUERP_CV[0].values.tolist(),
                        index=PUERP_CV.index)
PUERP_CV = pd.DataFrame(PUERP_CV[CODE].values.tolist(),
                        index=PUERP_CV.index).stack().reset_index().drop('level_2', axis=1)
PUERP_CV['indicator'] = 'puerperal_cerebrovascular_disorders'

PULM_EDEMA = pd.DataFrame.from_dict(PULM_EDEMA, orient='index').stack().to_frame()
PULM_EDEMA = pd.DataFrame(PULM_EDEMA[0].values.tolist(),
                          index=PULM_EDEMA.index)
PULM_EDEMA = pd.DataFrame(PULM_EDEMA[CODE].values.tolist(),
                          index=PULM_EDEMA.index).stack().reset_index().drop('level_2', axis=1)
PULM_EDEMA['indicator'] = 'pulmonary_edema_acute_heart_failure'

ANEST_COMP = pd.DataFrame.from_dict(ANEST_COMP, orient='index').stack().to_frame()
ANEST_COMP = pd.DataFrame(ANEST_COMP[0].values.tolist(),
                          index=ANEST_COMP.index)
ANEST_COMP = pd.DataFrame(ANEST_COMP[CODE].values.tolist(),
                          index=ANEST_COMP.index).stack().reset_index().drop('level_2', axis=1)
ANEST_COMP['indicator'] = 'severe_anesthesia_complications'

SEPSIS = pd.DataFrame.from_dict(SEPSIS, orient='index').stack().to_frame()
SEPSIS = pd.DataFrame(SEPSIS[0].values.tolist(),
                      index=SEPSIS.index)
SEPSIS = pd.DataFrame(SEPSIS[CODE].values.tolist(),
                      index=SEPSIS.index).stack().reset_index().drop('level_2', axis=1)
SEPSIS['indicator'] = 'SEPSIS'

SHOCK = pd.DataFrame.from_dict(SHOCK, orient='index').stack().to_frame()
SHOCK = pd.DataFrame(SHOCK[0].values.tolist(),
                     index=SHOCK.index)
SHOCK = pd.DataFrame(SHOCK[CODE].values.tolist(),
                     index=SHOCK.index).stack().reset_index().drop('level_2', axis=1)
SHOCK['indicator'] = 'SHOCK'

SICKLE_CELL = pd.DataFrame.from_dict(SICKLE_CELL, orient='index').stack().to_frame()
SICKLE_CELL = pd.DataFrame(SICKLE_CELL[0].values.tolist(),
                           index=SICKLE_CELL.index)
SICKLE_CELL = pd.DataFrame(SICKLE_CELL[CODE].values.tolist(),
                           index=SICKLE_CELL.index).stack().reset_index().drop('level_2', axis=1)
SICKLE_CELL['indicator'] = 'sickle_cell_disease_with_crisis'

EMBOLISM = pd.DataFrame.from_dict(EMBOLISM, orient='index').stack().to_frame()
EMBOLISM = pd.DataFrame(EMBOLISM[0].values.tolist(),
                        index=EMBOLISM.index)
EMBOLISM = pd.DataFrame(EMBOLISM[CODE].values.tolist(),
                        index=EMBOLISM.index).stack().reset_index().drop('level_2', axis=1)
EMBOLISM['indicator'] = 'air_and_thrombotic_embolism'

HYSTERECTOMY = pd.DataFrame.from_dict(HYSTERECTOMY, orient='index').stack().to_frame()
HYSTERECTOMY = pd.DataFrame(HYSTERECTOMY[0].values.tolist(),
                            index=HYSTERECTOMY.index)
HYSTERECTOMY = pd.DataFrame(HYSTERECTOMY[CODE].values.tolist(),
                            index=HYSTERECTOMY.index).stack().reset_index().drop('level_2', axis=1)
HYSTERECTOMY['indicator'] = 'HYSTERECTOMY'

TRACH = pd.DataFrame.from_dict(TRACH, orient='index').stack().to_frame()
TRACH = pd.DataFrame(TRACH[0].values.tolist(),
                     index=TRACH.index)
TRACH = pd.DataFrame(TRACH[CODE].values.tolist(),
                     index=TRACH.index).stack().reset_index().drop('level_2', axis=1)
TRACH['indicator'] = 'temporary_tracheostomy'

VENT = pd.DataFrame.from_dict(VENT, orient='index').stack().to_frame()
VENT = pd.DataFrame(VENT[0].values.tolist(),
                    index=VENT.index)
VENT = pd.DataFrame(VENT[CODE].values.tolist(),
                    index=VENT.index).stack().reset_index().drop('level_2', axis=1)
VENT['indicator'] = 'ventilation'

TRANSFUSION = pd.DataFrame.from_dict(TRANSFUSION, orient='index').stack().to_frame()
TRANSFUSION = pd.DataFrame(TRANSFUSION[0].values.tolist(),
                           index=TRANSFUSION.index)
TRANSFUSION = pd.DataFrame(TRANSFUSION[CODE].values.tolist(),
                           index=TRANSFUSION.index).stack().reset_index().drop('level_2', axis=1)

SMM_COLUMNS = ['smm_type', 'smm_version', 'smm_code', 'indicator']
ACUTE_MI.columns = SMM_COLUMNS
ANEUR.columns = SMM_COLUMNS
RENAL.columns = SMM_COLUMNS
ADULT_RDS.columns = SMM_COLUMNS
AMNIOTIC_EMB.columns = SMM_COLUMNS
CARD_ARREST.columns = SMM_COLUMNS
CARDIAC_RHYTHM.columns = SMM_COLUMNS
INTRA_COAG.columns = SMM_COLUMNS
ECLAMPSIA.columns = SMM_COLUMNS
HEART_FAIL.columns = SMM_COLUMNS
PUERP_CV.columns = SMM_COLUMNS
PULM_EDEMA.columns = SMM_COLUMNS
ANEST_COMP.columns = SMM_COLUMNS
SEPSIS.columns = SMM_COLUMNS
SHOCK.columns = SMM_COLUMNS
SICKLE_CELL.columns = SMM_COLUMNS
EMBOLISM.columns = SMM_COLUMNS
HYSTERECTOMY.columns = SMM_COLUMNS
TRACH.columns = SMM_COLUMNS
VENT.columns = SMM_COLUMNS
TRANSFUSION.columns = SMM_COLUMNS[:-1]

_SMM = pd.concat([ACUTE_MI,
                  ANEUR,
                  RENAL,
                  ADULT_RDS,
                  AMNIOTIC_EMB,
                  CARD_ARREST,
                  CARDIAC_RHYTHM,
                  INTRA_COAG,
                  ECLAMPSIA,
                  HEART_FAIL,
                  PUERP_CV,
                  PULM_EDEMA,
                  ANEST_COMP,
                  SEPSIS,
                  SHOCK,
                  SICKLE_CELL,
                  EMBOLISM,
                  HYSTERECTOMY,
                  TRACH,
                  VENT,
                  ])

_SMM['smm'] = True
TRANSFUSION['TRANSFUSION'] = True
