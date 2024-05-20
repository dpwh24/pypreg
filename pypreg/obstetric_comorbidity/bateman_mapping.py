"""
Source material codes have been translated into regex.
They include the top-level CODE where feasible to account for idiosyncracies in different secondary data sources.

Codes are sourced from:
Bateman BT, Mhyre JM, Hernandez-Diaz S, Huybrechts KF, Fischer MA, Creanga AA, Callaghan WM, Gagne JJ.
    Development of a comorbidity index for use in obstetric patients. Obstet Gynecol. 2013 Nov;122(5):957-965.
    doi: 10.1097/AOG.0b013e3182a603bb. PMID: 24104771; PMCID: PMC3829199.
"""

import pandas as pd

version = 'ICD9'

# ======================
# Pulmonary hypertension
# ======================
pulm_ht = dict()
pulm_ht[version] = (
    "416[0,8,9].*",
)

# ======================
# Placenta previa
# ======================
placenta_prev = dict()
placenta_prev[version] = (
    "641[0,1].*",
)

# ======================
# Sickle cell
# ======================
sickle_cell = dict()
sickle_cell[version] = (
    "282[4,6].*",
)

# ======================
# Gestational hypertension
# ======================
gest_ht = dict()
gest_ht[version] = (
    "6423.*",
)

# ======================
# Mild preeclampsia or unspecified preeclampsia
# ======================
mild_pe = dict()
mild_pe[version] = (
    "642[4,7].*",
)

# ======================
# Severe preeclampsia / ECLAMPSIA
# ======================
eclampsia = dict()
eclampsia[version] = (
    "642[5,6].*",
)

# ======================
# Chronic RENAL disease
# ======================
renal_disease = dict()
renal_disease[version] = (
    "58[1-3,5,7,8].*",
    "6462.*",
)

# ======================
# Preexisting hypertension
# ======================
hypertension = dict()
hypertension[version] = (
    "40[1-5].*",
    "642[0-2,7].*",
)

# ======================
# Chronic ischemic heart disease
# ======================
ischemic_hd = dict()
ischemic_hd[version] = (
    "41[2-4].*",
)

# ======================
# Congenital heart disease
# ======================
congenital_hd = dict()
congenital_hd[version] = (
    "74([5-6]|7[0-4]).*",
)

# ======================
# Systemic lupus erythematosus
# ======================
lupus = dict()
lupus[version] = (
    "7100.*",
)

# ======================
# Human immunodeficiency virus
# ======================
hiv = dict()
hiv[version] = (
    "042.*",
    "V08.*",
)

# ======================
# Multiple gestation
# ======================
multiple_gest = dict()
multiple_gest[version] = (
    "V27[2-8].*",
    "651.*",
)

# ======================
# Drug abuse
# ======================
drug_abuse = dict()
drug_abuse[version] = (
    "30(4|5[2-9]).*",
    "6483.*",
)

# ======================
# Alcohol abuse
# ======================
alcohol_abuse = dict()
alcohol_abuse[version] = (
    "291.*",
    "30(3|50).*",
)

# ======================
# Tobacco abuse
# ======================
tobacco_abuse = dict()
tobacco_abuse[version] = (
    "3051.*",
    "6490.*",
)

# ======================
# Cardiac valvular disease
# ======================
card_valv = dict()
card_valv[version] = (
    "39[4-7].*",
    "424.*",
)

# ======================
# Chronic congestive heart failure
# ======================
congestive_hf = dict()
congestive_hf[version] = (
    "428[2-4][2-3].*",
)

# ======================
# Asthma
# ======================
asthma = dict()
asthma[version] = (
    "493.*",
)

# ======================
# Preexisting diabetes mellitus
# ======================
diabetes = dict()
diabetes[version] = (
    "250.*",
    "6480.*",
)

# ======================
# Gestational diabetes mellitus
# ======================
gest_dm = dict()
gest_dm[version] = (
    "6488.*",
)

# ======================
# Obesity
# ======================
obesity = dict()
obesity[version] = (
    "2780.*",
    "6491.*",
    "V85[3-4].*",
)

# ======================
# Cystic fibrosis
# ======================
cystic_fibrosis = dict()
cystic_fibrosis[version] = (
    "2770.*",
)

# ======================
# Previous cesarean delivery
# ======================
previous_csec = dict()
previous_csec[version] = (
    "6542.*",
)

# ======================
# Convert to Pandas
# ======================
pulm_ht = pd.DataFrame.from_dict(pulm_ht, orient='index').stack().to_frame()
pulm_ht = pulm_ht.reset_index().drop('level_1', axis=1)
pulm_ht['indicator'] = 'pulmonary hypertension'

placenta_prev = pd.DataFrame.from_dict(placenta_prev, orient='index').stack().to_frame()
placenta_prev = placenta_prev.reset_index().drop('level_1', axis=1)
placenta_prev['indicator'] = 'placenta previa'

sickle_cell = pd.DataFrame.from_dict(sickle_cell, orient='index').stack().to_frame()
sickle_cell = sickle_cell.reset_index().drop('level_1', axis=1)
sickle_cell['indicator'] = 'sickle cell disease'

gest_ht = pd.DataFrame.from_dict(gest_ht, orient='index').stack().to_frame()
gest_ht = gest_ht.reset_index().drop('level_1', axis=1)
gest_ht['indicator'] = 'gestational hypertension'

mild_pe = pd.DataFrame.from_dict(mild_pe, orient='index').stack().to_frame()
mild_pe = mild_pe.reset_index().drop('level_1', axis=1)
mild_pe['indicator'] = 'mild preeclampsia'

eclampsia = pd.DataFrame.from_dict(eclampsia, orient='index').stack().to_frame()
eclampsia = eclampsia.reset_index().drop('level_1', axis=1)
eclampsia['indicator'] = 'ECLAMPSIA'

renal_disease = pd.DataFrame.from_dict(renal_disease, orient='index').stack().to_frame()
renal_disease = renal_disease.reset_index().drop('level_1', axis=1)
renal_disease['indicator'] = 'chronic RENAL disease'

hypertension = pd.DataFrame.from_dict(hypertension, orient='index').stack().to_frame()
hypertension = hypertension.reset_index().drop('level_1', axis=1)
hypertension['indicator'] = 'preexisting hypertension'

ischemic_hd = pd.DataFrame.from_dict(ischemic_hd, orient='index').stack().to_frame()
ischemic_hd = ischemic_hd.reset_index().drop('level_1', axis=1)
ischemic_hd['indicator'] = 'chronic ischemic heart disease'

congenital_hd = pd.DataFrame.from_dict(congenital_hd, orient='index').stack().to_frame()
congenital_hd = congenital_hd.reset_index().drop('level_1', axis=1)
congenital_hd['indicator'] = 'congenital heart disease'

lupus = pd.DataFrame.from_dict(lupus, orient='index').stack().to_frame()
lupus = lupus.reset_index().drop('level_1', axis=1)
lupus['indicator'] = 'lupus'

hiv = pd.DataFrame.from_dict(hiv, orient='index').stack().to_frame()
hiv = hiv.reset_index().drop('level_1', axis=1)
hiv['indicator'] = 'hiv'

multiple_gest = pd.DataFrame.from_dict(multiple_gest, orient='index').stack().to_frame()
multiple_gest = multiple_gest.reset_index().drop('level_1', axis=1)
multiple_gest['indicator'] = 'multiple gestation'

drug_abuse = pd.DataFrame.from_dict(drug_abuse, orient='index').stack().to_frame()
drug_abuse = drug_abuse.reset_index().drop('level_1', axis=1)
drug_abuse['indicator'] = 'drug abuse'

alcohol_abuse = pd.DataFrame.from_dict(alcohol_abuse, orient='index').stack().to_frame()
alcohol_abuse = alcohol_abuse.reset_index().drop('level_1', axis=1)
alcohol_abuse['indicator'] = 'alcohol abuse'

tobacco_abuse = pd.DataFrame.from_dict(tobacco_abuse, orient='index').stack().to_frame()
tobacco_abuse = tobacco_abuse.reset_index().drop('level_1', axis=1)
tobacco_abuse['indicator'] = 'tobacco use'

card_valv = pd.DataFrame.from_dict(card_valv, orient='index').stack().to_frame()
card_valv = card_valv.reset_index().drop('level_1', axis=1)
card_valv['indicator'] = 'cardiac valvular disease'

congestive_hf = pd.DataFrame.from_dict(congestive_hf, orient='index').stack().to_frame()
congestive_hf = congestive_hf.reset_index().drop('level_1', axis=1)
congestive_hf['indicator'] = 'chronic congestive heart failure'

asthma = pd.DataFrame.from_dict(asthma, orient='index').stack().to_frame()
asthma = asthma.reset_index().drop('level_1', axis=1)
asthma['indicator'] = 'asthma'

diabetes = pd.DataFrame.from_dict(diabetes, orient='index').stack().to_frame()
diabetes = diabetes.reset_index().drop('level_1', axis=1)
diabetes['indicator'] = 'preexisting diabetes'

gest_dm = pd.DataFrame.from_dict(gest_dm, orient='index').stack().to_frame()
gest_dm = gest_dm.reset_index().drop('level_1', axis=1)
gest_dm['indicator'] = 'gestational diabetes'

obesity = pd.DataFrame.from_dict(obesity, orient='index').stack().to_frame()
obesity = obesity.reset_index().drop('level_1', axis=1)
obesity['indicator'] = 'obesity'

cystic_fibrosis = pd.DataFrame.from_dict(cystic_fibrosis, orient='index').stack().to_frame()
cystic_fibrosis = cystic_fibrosis.reset_index().drop('level_1', axis=1)
cystic_fibrosis['indicator'] = 'cystic fibrosis'

previous_csec = pd.DataFrame.from_dict(previous_csec, orient='index').stack().to_frame()
previous_csec = previous_csec.reset_index().drop('level_1', axis=1)
previous_csec['indicator'] = 'previous cesarean'


columns = ['VERSION', 'CODE', 'indicator']
pulm_ht.columns = columns
placenta_prev.columns = columns
sickle_cell.columns = columns
gest_ht.columns = columns
mild_pe.columns = columns
eclampsia.columns = columns
renal_disease.columns = columns
hypertension.columns = columns
ischemic_hd.columns = columns
congenital_hd.columns = columns
lupus.columns = columns
hiv.columns = columns
multiple_gest.columns = columns
drug_abuse.columns = columns
alcohol_abuse.columns = columns
tobacco_abuse.columns = columns
card_valv.columns = columns
congestive_hf.columns = columns
asthma.columns = columns
diabetes.columns = columns
gest_dm.columns = columns
obesity.columns = columns
cystic_fibrosis.columns = columns
previous_csec.columns = columns

age_category = ['<35',
                '35-39',
                '40-44',
                '>44']

weights = {pulm_ht['indicator'][0]: 4,
           placenta_prev['indicator'][0]: 2,
           sickle_cell['indicator'][0]: 3,
           gest_ht['indicator'][0]: 1,
           mild_pe['indicator'][0]: 2,
           eclampsia['indicator'][0]: 5,
           renal_disease['indicator'][0]: 1,
           hypertension['indicator'][0]: 1,
           ischemic_hd['indicator'][0]: 3,
           congenital_hd['indicator'][0]: 4,
           lupus['indicator'][0]: 2,
           hiv['indicator'][0]: 2,
           multiple_gest['indicator'][0]: 2,
           drug_abuse['indicator'][0]: 2,
           alcohol_abuse['indicator'][0]: 1,
           tobacco_abuse['indicator'][0]: 0,
           card_valv['indicator'][0]: 2,
           congestive_hf['indicator'][0]: 5,
           asthma['indicator'][0]: 1,
           diabetes['indicator'][0]: 1,
           gest_dm['indicator'][0]: 0,
           obesity['indicator'][0]: 0,
           cystic_fibrosis['indicator'][0]: 0,
           previous_csec['indicator'][0]: 1,
           age_category[1]: 1,
           age_category[2]: 2,
           age_category[3]: 3,
           }

weights = pd.DataFrame.from_dict(weights, orient='index', columns=['weight'])

bateman_map = pd.concat([
    pulm_ht,
    placenta_prev,
    sickle_cell,
    gest_ht,
    mild_pe,
    eclampsia,
    renal_disease,
    hypertension,
    ischemic_hd,
    congenital_hd,
    lupus,
    hiv,
    multiple_gest,
    drug_abuse,
    alcohol_abuse,
    tobacco_abuse,
    card_valv,
    congestive_hf,
    asthma,
    diabetes,
    gest_dm,
    obesity,
    cystic_fibrosis,
    previous_csec
])

bateman_map = bateman_map.merge(weights,
                                how='right',
                                left_on='indicator',
                                right_index=True)
