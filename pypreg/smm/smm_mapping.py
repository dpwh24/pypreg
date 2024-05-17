"""
Update 03Jan2024
Codes in FAD SAS code do not appear to be current with CDC nor HCUP definitions.
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
Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK An Expanded Obstetric Comorbidity Scoring System
    for Predicting Severe Maternal Morbidity. 2020-08. Obstetrics & Gynecology, Vol. 136, No. 3
    Ovid Technologies (Wolters Kluwer Health) p. 440-449

"""


import pandas as pd

icd9 = 'ICD9'
icd10 = 'ICD10'

# ======================
# Acute Myocardial Infarction
# ======================
acute_mi = dict()

type = 'DX'
version = icd9
code = 'code'

acute_mi[type] = dict()
acute_mi[type][version] = dict()
acute_mi[type][version][code] = (
    r"^410.*",
)

version = icd10
acute_mi[type][version] = dict()
acute_mi[type][version][code] = (
    r"^I21.*",
    r"^I22.*",
)

# ======================
# Aneurysm
# ======================
aneur = dict()

version = icd9

aneur[type] = dict()
aneur[type][version] = dict()
aneur[type][version][code] = (
    "^441.*",
)

version = icd10
aneur[type][version] = dict()
aneur[type][version][code] = (
    r"^I71.*",
    r"^I790$",
)

# ======================
# Acute Renal Failure
# ======================
renal = dict()

type = 'DX'
version = icd9
code = 'code'

renal[type] = dict()
renal[type][version] = dict()
renal[type][version][code] = (
    r"^584[5-9]$",
    r"^6693.*",
)

version = icd10
renal[type][version] = dict()
renal[type][version][code] = (
    "^N17.*",
    "^O904$",
)

# ======================
# Adult Respiratory Distress Syndrome
# ======================
adult_rds = dict()

type = 'DX'
version = icd9
code = 'code'

adult_rds[type] = dict()
adult_rds[type][version] = dict()
adult_rds[type][version][code] = (
    r"^5185.*",
    r"^5188[124]$",
    r"^7991$",
)

version = icd10
adult_rds[type][version] = dict()
adult_rds[type][version][code] = (
    r"^J80$",
    r"^J95([1-3]$|82.*)",
    r"^J96[029].*",
    r"^R0(603|92)$",
)

# ======================
# Amniotic fluid embolism
# ======================
amniotic_emb = dict()

type = 'DX'
version = icd9
code = 'code'

amniotic_emb[type] = dict()
amniotic_emb[type][version] = dict()
amniotic_emb[type][version][code] = (
    r"^6731.*",
)

version = icd10
amniotic_emb[type][version] = dict()
amniotic_emb[type][version][code] = (
    r"^O881(1[239]|[23])$",
)

# ======================
# Cardiac arrest/ventricular fibrilation
# ======================
card_arrest = dict()

type = 'DX'
version = icd9
code = 'code'

card_arrest[type] = dict()
card_arrest[type][version] = dict()
card_arrest[type][version][code] = (
    r"^427(4[12]|5)$",
)

version = icd10
card_arrest[type][version] = dict()
card_arrest[type][version][code] = (
    r"^I46.*",
    r"^I490.*",
)

# ======================
# Conversion of cardiac rhythm
# ======================
cardiac_rhythm = dict()

type = 'PX'
version = icd9
code = 'code'

cardiac_rhythm[type] = dict()
cardiac_rhythm[type][version] = dict()
cardiac_rhythm[type][version][code] = (
    r"^996.*",
)

version = icd10
cardiac_rhythm[type][version] = dict()
cardiac_rhythm[type][version][code] = (
    r"^5A2204Z$",
    r"^5A12012$",
)

# ======================
# Disseminated intravascular coagulation
# ======================
intra_coag = dict()

type = 'DX'
version = icd9
code = 'code'

intra_coag[type] = dict()
intra_coag[type][version] = dict()
intra_coag[type][version][code] = (
    r"^286[69]$",
    r"^6413.*",
    r"^6663.*",
)

version = icd10
intra_coag[type][version] = dict()
intra_coag[type][version][code] = (
    r"^D6(5|8[89])$",
    r"^O4[56]0[0-29][239]$",
    r"^O670$",
    r"^O723$",
)

# ======================
# Eclampsia
# ======================
eclampsia = dict()

type = 'DX'
version = icd9
code = 'code'

eclampsia[type] = dict()
eclampsia[type][version] = dict()
eclampsia[type][version][code] = (
    r"^6426.*",
)

version = icd10
eclampsia[type][version] = dict()
eclampsia[type][version][code] = (
    r"^O15.*",
)

# ======================
# Heart failure / arrest during surgery or procedure
# ======================
heart_fail = dict()

type = 'DX'
version = icd9
code = 'code'

heart_fail[type] = dict()
heart_fail[type][version] = dict()
heart_fail[type][version][code] = (
    r"^9971$",
)

version = icd10
heart_fail[type][version] = dict()
heart_fail[type][version][code] = (
    r"^I97(1[23]|71)[01]$",
)

# ======================
# Puerperal cerebrovascular disorders
# ======================
puerp_cv = dict()

type = 'DX'
version = icd9
code = 'code'

puerp_cv[type] = dict()
puerp_cv[type][version] = dict()
puerp_cv[type][version][code] = (
    r"^0463$",
    r"^34839$",
    r"^36234$",
    r"^43[0-7].*",
    r"^67(15|40).*",
    r"^99702$",
)

version = icd10
puerp_cv[type][version] = dict()
puerp_cv[type][version][code] = (
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
pulm_edema = dict()

type = 'DX'
version = icd9
code = 'code'

pulm_edema[type] = dict()
pulm_edema[type][version] = dict()
pulm_edema[type][version][code] = (
    r"^5184$",
    r"^428([01]|[2-4][013]|9)$",
)

version = icd10
pulm_edema[type][version] = dict()
pulm_edema[type][version][code] = (
    r"^J810$",
    r"^I50([19]|[2-4][013]|81[0134]|8[2-49])$",
)

# ======================
# Severe anesthesia complications
# ======================
anest_comp = dict()

type = 'DX'
version = icd9
code = 'code'

anest_comp[type] = dict()
anest_comp[type][version] = dict()
anest_comp[type][version][code] = (
    r"^668[0-2].*",
    r"^995(4|86)$",
)

version = icd10
anest_comp[type][version] = dict()
anest_comp[type][version][code] = (
    r"^O29(1[129]|2[19])[239]$",
    r"^O74[0-3]$",
    r"^O89(0.*|[12]$)",
    r"^T88[23]XXA$",
)

# ======================
# Sepsis
# ======================
sepsis = dict()

type = 'DX'
version = icd9
code = 'code'

sepsis[type] = dict()
sepsis[type][version] = dict()
sepsis[type][version][code] = (
    r"^038.*",
    r"^6702.*",
    r"^99802$",
    r"^9959[12]$",
    r"^78552$",
    r"^449$",
)

version = icd10
sepsis[type][version] = dict()
sepsis[type][version][code] = (
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
shock = dict()

type = 'DX'
version = icd9
code = 'code'

shock[type] = dict()
shock[type][version] = dict()
shock[type][version][code] = (
    r"^6691.*",
    r"^7855[019]$",
    r"^99(50|80[019]?)$",
)

version = icd10
shock[type][version] = dict()
shock[type][version][code] = (
    r"^O751$",
    r"^R57.*",
    r"^T(782X|886X|811[019])XA$",
)

# ======================
# Sickle cell disease with crisis
# ======================
sickle_cell = dict()

type = 'DX'
version = icd9
code = 'code'

sickle_cell[type] = dict()
sickle_cell[type][version] = dict()
sickle_cell[type][version][code] = (
    r"^282(42|6[249])$",
    r"^28952$",
)

version = icd10
sickle_cell[type][version] = dict()
sickle_cell[type][version][code] = (
    r"^D57(0[0-2]|[248]1[129])$",
)

# ======================
# Air and thrombotic embolism
# ======================
embolism = dict()

type = 'DX'
version = icd9
code = 'code'

embolism[type] = dict()
embolism[type][version] = dict()
embolism[type][version][code] = (
    r"^415(0$|1.*)",
    r"^673[0238].*",
)

version = icd10
embolism[type][version] = dict()
embolism[type][version][code] = (
    r"^I26.*",
    r"^O88[0238](1[239]|[23])$",
    r"^T800XXA$",
)

# ======================
# Hysterectomy
# ======================
hysterectomy = dict()

type = 'PX'
version = icd9
code = 'code'

# Removing the top level codes consistent with AIM codesheet removes 63 occurences from HF data
hysterectomy[type] = dict()
hysterectomy[type][version] = dict()
hysterectomy[type][version][code] = (
    "^68([3-7]9?|9)$",
)

version = icd10
hysterectomy[type][version] = dict()
hysterectomy[type][version][code] = (
    r"^0UT9[07]Z[LZ]$",
)

# ======================
# Temporary tracheostomy
# ======================
trach = dict()

type = 'PX'
version = icd9
code = 'code'

trach[type] = dict()
trach[type][version] = dict()
trach[type][version][code] = (
    r"^311$",
)

version = icd10
trach[type][version] = dict()
trach[type][version][code] = (
    r"^0B11[034]F4$",
)

# ======================
# Ventilation
# ======================
vent = dict()

type = 'PX'
version = icd9
code = 'code'

vent[type] = dict()
vent[type][version] = dict()
vent[type][version][code] = (
    r"^967[0-2]$",
)

version = icd10
vent[type][version] = dict()
vent[type][version][code] = (
    r"^5A19[3-5]5Z$",
)

# ======================
# Transfusion
# ======================
transfusion = dict()

type = 'PX'
version = icd9
code = 'code'

transfusion[type] = dict()
transfusion[type][version] = dict()
transfusion[type][version][code] = (
    r"^990.*",
)

version = icd10
transfusion[type][version] = dict()
transfusion[type][version][code] = (
    r"^302[34][03][HK-NPRT][01]$",
)

# ======================
# Convert to Pandas
# ======================
acute_mi = pd.DataFrame.from_dict(acute_mi, orient='index').stack().to_frame()
acute_mi = pd.DataFrame(acute_mi[0].values.tolist(), index=acute_mi.index)
acute_mi = pd.DataFrame(acute_mi[code].values.tolist(), index=acute_mi.index).stack().reset_index().drop('level_2', axis=1)
acute_mi['indicator'] = 'acute_myocardial_infarction'

aneur = pd.DataFrame.from_dict(aneur, orient='index').stack().to_frame()
aneur = pd.DataFrame(aneur[0].values.tolist(), index=aneur.index)
aneur = pd.DataFrame(aneur[code].values.tolist(), index=aneur.index).stack().reset_index().drop('level_2', axis=1)
aneur['indicator'] = 'aneurysm'

renal = pd.DataFrame.from_dict(renal, orient='index').stack().to_frame()
renal = pd.DataFrame(renal[0].values.tolist(), index=renal.index)
renal = pd.DataFrame(renal[code].values.tolist(), index=renal.index).stack().reset_index().drop('level_2', axis=1)
renal['indicator'] = 'acute_renal_failure'

adult_rds = pd.DataFrame.from_dict(adult_rds, orient='index').stack().to_frame()
adult_rds = pd.DataFrame(adult_rds[0].values.tolist(), index=adult_rds.index)
adult_rds = pd.DataFrame(adult_rds[code].values.tolist(), index=adult_rds.index).stack().reset_index().drop('level_2', axis=1)
adult_rds['indicator'] = 'adult_respiratory_distress_syndrome'

amniotic_emb = pd.DataFrame.from_dict(amniotic_emb, orient='index').stack().to_frame()
amniotic_emb = pd.DataFrame(amniotic_emb[0].values.tolist(), index=amniotic_emb.index)
amniotic_emb = pd.DataFrame(amniotic_emb[code].values.tolist(), index=amniotic_emb.index).stack().reset_index().drop('level_2', axis=1)
amniotic_emb['indicator'] = 'amniotic_fluid_embolism'

card_arrest = pd.DataFrame.from_dict(card_arrest, orient='index').stack().to_frame()
card_arrest = pd.DataFrame(card_arrest[0].values.tolist(), index=card_arrest.index)
card_arrest = pd.DataFrame(card_arrest[code].values.tolist(), index=card_arrest.index).stack().reset_index().drop('level_2', axis=1)
card_arrest['indicator'] = 'cardiac_arrest_ventricular_fibrillation'

cardiac_rhythm = pd.DataFrame.from_dict(cardiac_rhythm, orient='index').stack().to_frame()
cardiac_rhythm = pd.DataFrame(cardiac_rhythm[0].values.tolist(), index=cardiac_rhythm.index)
cardiac_rhythm = pd.DataFrame(cardiac_rhythm[code].values.tolist(), index=cardiac_rhythm.index).stack().reset_index().drop('level_2', axis=1)
cardiac_rhythm['indicator'] = 'conversion_of_cardiac_rhythm'

intra_coag = pd.DataFrame.from_dict(intra_coag, orient='index').stack().to_frame()
intra_coag = pd.DataFrame(intra_coag[0].values.tolist(), index=intra_coag.index)
intra_coag = pd.DataFrame(intra_coag[code].values.tolist(), index=intra_coag.index).stack().reset_index().drop('level_2', axis=1)
intra_coag['indicator'] = 'disseminated_intravascular_coagulation'

eclampsia = pd.DataFrame.from_dict(eclampsia, orient='index').stack().to_frame()
eclampsia = pd.DataFrame(eclampsia[0].values.tolist(), index=eclampsia.index)
eclampsia = pd.DataFrame(eclampsia[code].values.tolist(), index=eclampsia.index).stack().reset_index().drop('level_2', axis=1)
eclampsia['indicator'] = 'eclampsia'

heart_fail = pd.DataFrame.from_dict(heart_fail, orient='index').stack().to_frame()
heart_fail = pd.DataFrame(heart_fail[0].values.tolist(), index=heart_fail.index)
heart_fail = pd.DataFrame(heart_fail[code].values.tolist(), index=heart_fail.index).stack().reset_index().drop('level_2', axis=1)
heart_fail['indicator'] = 'heart_failure_arrest_during_surgery_or_procedure'

puerp_cv = pd.DataFrame.from_dict(puerp_cv, orient='index').stack().to_frame()
puerp_cv = pd.DataFrame(puerp_cv[0].values.tolist(), index=puerp_cv.index)
puerp_cv = pd.DataFrame(puerp_cv[code].values.tolist(), index=puerp_cv.index).stack().reset_index().drop('level_2', axis=1)
puerp_cv['indicator'] = 'puerperal_cerebrovascular_disorders'

pulm_edema = pd.DataFrame.from_dict(pulm_edema, orient='index').stack().to_frame()
pulm_edema = pd.DataFrame(pulm_edema[0].values.tolist(), index=pulm_edema.index)
pulm_edema = pd.DataFrame(pulm_edema[code].values.tolist(), index=pulm_edema.index).stack().reset_index().drop('level_2', axis=1)
pulm_edema['indicator'] = 'pulmonary_edema_acute_heart_failure'

anest_comp = pd.DataFrame.from_dict(anest_comp, orient='index').stack().to_frame()
anest_comp = pd.DataFrame(anest_comp[0].values.tolist(), index=anest_comp.index)
anest_comp = pd.DataFrame(anest_comp[code].values.tolist(), index=anest_comp.index).stack().reset_index().drop('level_2', axis=1)
anest_comp['indicator'] = 'severe_anesthesia_complications'

sepsis = pd.DataFrame.from_dict(sepsis, orient='index').stack().to_frame()
sepsis = pd.DataFrame(sepsis[0].values.tolist(), index=sepsis.index)
sepsis = pd.DataFrame(sepsis[code].values.tolist(), index=sepsis.index).stack().reset_index().drop('level_2', axis=1)
sepsis['indicator'] = 'sepsis'

shock = pd.DataFrame.from_dict(shock, orient='index').stack().to_frame()
shock = pd.DataFrame(shock[0].values.tolist(), index=shock.index)
shock = pd.DataFrame(shock[code].values.tolist(), index=shock.index).stack().reset_index().drop('level_2', axis=1)
shock['indicator'] = 'shock'

sickle_cell = pd.DataFrame.from_dict(sickle_cell, orient='index').stack().to_frame()
sickle_cell = pd.DataFrame(sickle_cell[0].values.tolist(), index=sickle_cell.index)
sickle_cell = pd.DataFrame(sickle_cell[code].values.tolist(), index=sickle_cell.index).stack().reset_index().drop('level_2', axis=1)
sickle_cell['indicator'] = 'sickle_cell_disease_with_crisis'

embolism = pd.DataFrame.from_dict(embolism, orient='index').stack().to_frame()
embolism = pd.DataFrame(embolism[0].values.tolist(), index=embolism.index)
embolism = pd.DataFrame(embolism[code].values.tolist(), index=embolism.index).stack().reset_index().drop('level_2', axis=1)
embolism['indicator'] = 'air_and_thrombotic_embolism'

hysterectomy = pd.DataFrame.from_dict(hysterectomy, orient='index').stack().to_frame()
hysterectomy = pd.DataFrame(hysterectomy[0].values.tolist(), index=hysterectomy.index)
hysterectomy = pd.DataFrame(hysterectomy[code].values.tolist(), index=hysterectomy.index).stack().reset_index().drop('level_2', axis=1)
hysterectomy['indicator'] = 'hysterectomy'

trach = pd.DataFrame.from_dict(trach, orient='index').stack().to_frame()
trach = pd.DataFrame(trach[0].values.tolist(), index=trach.index)
trach = pd.DataFrame(trach[code].values.tolist(), index=trach.index).stack().reset_index().drop('level_2', axis=1)
trach['indicator'] = 'temporary_tracheostomy'

vent = pd.DataFrame.from_dict(vent, orient='index').stack().to_frame()
vent = pd.DataFrame(vent[0].values.tolist(), index=vent.index)
vent = pd.DataFrame(vent[code].values.tolist(), index=vent.index).stack().reset_index().drop('level_2', axis=1)
vent['indicator'] = 'ventilation'

transfusion = pd.DataFrame.from_dict(transfusion, orient='index').stack().to_frame()
transfusion = pd.DataFrame(transfusion[0].values.tolist(), index=transfusion.index)
transfusion = pd.DataFrame(transfusion[code].values.tolist(), index=transfusion.index).stack().reset_index().drop('level_2', axis=1)

columns = ['smm_type', 'smm_version', 'smm_code', 'indicator']
acute_mi.columns = columns
aneur.columns = columns
renal.columns = columns
adult_rds.columns = columns
amniotic_emb.columns = columns
card_arrest.columns = columns
cardiac_rhythm.columns = columns
intra_coag.columns = columns
eclampsia.columns = columns
heart_fail.columns = columns
puerp_cv.columns = columns
pulm_edema.columns = columns
anest_comp.columns = columns
sepsis.columns = columns
shock.columns = columns
sickle_cell.columns = columns
embolism.columns = columns
hysterectomy.columns = columns
trach.columns = columns
vent.columns = columns
transfusion.columns = columns[:-1]

_smm = pd.concat([acute_mi,
                  aneur,
                  renal,
                  adult_rds,
                  amniotic_emb,
                  card_arrest,
                  cardiac_rhythm,
                  intra_coag,
                  eclampsia,
                  heart_fail,
                  puerp_cv,
                  pulm_edema,
                  anest_comp,
                  sepsis,
                  shock,
                  sickle_cell,
                  embolism,
                  hysterectomy,
                  trach,
                  vent,
                  ])

_smm['smm'] = True
transfusion['transfusion'] = True
