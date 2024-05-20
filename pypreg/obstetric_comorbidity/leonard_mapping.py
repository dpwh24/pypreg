"""
Source material codes have been translated into regex.
They include the top-level CODE where feasible to account for idiosyncracies in different secondary data sources.

Codes are sourced from:
Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK.
    An Expanded Obstetric Comorbidity Scoring System for Predicting Severe Maternal Morbidity. Obstet Gynecol.
    2020 Sep;136(3):440-449. doi: 10.1097/AOG.0000000000004022. PMID: 32769656; PMCID: PMC7523732.
"""

import pandas as pd

version = 'ICD10'

# ======================
# Gestational diabetes
# ======================
gest_dm = dict()
gest_dm[version] = (
    "O244.*",
)

# ======================
# HIV / AIDS
# ======================
hiv = dict()
hiv[version] = (
    "O987.*",
    "B20",
)

# ======================
# Preexisting diabetes mellitus
# ======================
diabetes = dict()
diabetes[version] = (
    "E(0[8-9]|1[0,1,3]).*",
    "O24[0,1,3,8,9].*",
    "Z794.*",
)

# ======================
# Previous cesarean birth
# ======================
cesarean = dict()
cesarean[version] = (
    "O3421.*",
)

# ======================
# Pulmonary hypertension
# ======================
pulm_ht = dict()
pulm_ht[version] = (
    "I27[0,2].*",
)

# ======================
# Twin/multiple pregnancy
# ======================
multiple_gest = dict()
multiple_gest[version] = (
    "O3[0-1].*",
    "Z37[2-7].*",
)

# ======================
# Asthma
# ======================
asthma = dict()
asthma[version] = (
    "O995.*",
    "J45([2-3][1-2]|[4-5]|90[1-2]).*",
)

# ======================
# Bleeding disorder
# ======================
bleeding = dict()
bleeding[version] = (
    "D6[6-9].*",
)

# ======================
# Obesity
# ======================
obesity = dict()
obesity[version] = (
    "Z684.*",
)

# ======================
# Cardiac disease
# ======================
cardiac_disease = dict()
cardiac_disease[version] = (
    "I(0[5-9]|1[1-3,5,6]|2[0,5]|278|3[0-9]|4[1,4-9]|50[2-4][2-3]|5081[2-3]).*",
    "O994[1-2].*",
    "Q2[0-4].*",
)

# ======================
# Chronic hypertension
# ======================
hypertension = dict()
hypertension[version] = (
    "O1[0-1].*",
    "I10.*",
)

# ======================
# Chronic RENAL disease
# ======================
renal = dict()
renal[version] = (
    "O2683.*",
    "I1[2-3].*",
    "N(0[3-5,7,8]|11[1,8,9]|18|25[0-1,9]|258[1,9]|269).*",
)

# ======================
# Connective tissue or autoimmune disease
# ======================
autoimmune = dict()
autoimmune[version] = (
    "M3[0-6].*",
)

# ======================
# Placenta previa
# ======================
placenta_previa = dict()
placenta_previa[version] = (
    "O44[0-3]3",
)

# ======================
# Preeclampsia
# ======================
preeclampsia = dict()
preeclampsia[version] = (
    "O1(1|4[1-2]).*",
)

# ======================
# Mild preeclampsia
# ======================
mild_preeclampsia = dict()
mild_preeclampsia[version] = (
    "O1(3|4[0,9]).*",
)

# ======================
# Substance use disorder
# ======================
substance_use = dict()
substance_use[version] = (
    "F1[0-9].*",
    "O993[1-2].*",
)

# ======================
# Anemia
# ======================
anemia = dict()
anemia[version] = (
    "O990[1-2].*",
    "D5([0,5,6,8,9]|7[1,3]|7[2,4,8]0).*",
)

# ======================
# Bariatric surgery
# ======================
bariatric = dict()
bariatric[version] = (
    "O9984.*",
)

# ======================
# Gastrointestinal disease
# ======================
gi_disease = dict()
gi_disease[version] = (
    "K.*",
    "O996.*",
    "O266.*"
)

# ======================
# Mental health disorder
# ======================
mental_health = dict()
mental_health[version] = (
    "O9934.*",
    "F[2-3][0-9].*",
)

# ======================
# Neuromuscular disease
# ======================
neuromuscular = dict()
neuromuscular[version] = (
    "O9935.*",
    "G[4,7]0.*",
)

# ======================
# Placental abruption
# ======================
abruption = dict()
abruption[version] = (
    "O45.*",
)

# ======================
# Placental accreta spectrum
# ======================
accreta = dict()
accreta[version] = (
    "O432.*",
)

# ======================
# Preterm birth
# ======================
preterm = dict()
preterm[version] = (
    "Z3A(2[0-9]|3[0-6]).*",
)

# ======================
# Thyrotoxicosis
# ======================
thyrotoxicosis = dict()
thyrotoxicosis[version] = (
    "E05.*",
)

# ======================
# Convert to Pandas
# ======================
gest_dm = pd.DataFrame.from_dict(gest_dm, orient='index').stack().to_frame()
gest_dm = gest_dm.reset_index().drop('level_1', axis=1)
gest_dm['indicator'] = 'gestational diabetes'

hiv = pd.DataFrame.from_dict(hiv, orient='index').stack().to_frame()
hiv = hiv.reset_index().drop('level_1', axis=1)
hiv['indicator'] = 'hiv'

diabetes = pd.DataFrame.from_dict(diabetes, orient='index').stack().to_frame()
diabetes = diabetes.reset_index().drop('level_1', axis=1)
diabetes['indicator'] = 'preexisting diabetes'

cesarean = pd.DataFrame.from_dict(cesarean, orient='index').stack().to_frame()
cesarean = cesarean.reset_index().drop('level_1', axis=1)
cesarean['indicator'] = 'previous cesarean'

pulm_ht = pd.DataFrame.from_dict(pulm_ht, orient='index').stack().to_frame()
pulm_ht = pulm_ht.reset_index().drop('level_1', axis=1)
pulm_ht['indicator'] = 'pulmonary hypertension'

multiple_gest = pd.DataFrame.from_dict(multiple_gest, orient='index').stack().to_frame()
multiple_gest = multiple_gest.reset_index().drop('level_1', axis=1)
multiple_gest['indicator'] = 'multiple gestation'

asthma = pd.DataFrame.from_dict(asthma, orient='index').stack().to_frame()
asthma = asthma.reset_index().drop('level_1', axis=1)
asthma['indicator'] = 'asthma'

bleeding = pd.DataFrame.from_dict(bleeding, orient='index').stack().to_frame()
bleeding = bleeding.reset_index().drop('level_1', axis=1)
bleeding['indicator'] = 'bleeding disorder'

obesity = pd.DataFrame.from_dict(obesity, orient='index').stack().to_frame()
obesity = obesity.reset_index().drop('level_1', axis=1)
obesity['indicator'] = 'obesity'

cardiac_disease = pd.DataFrame.from_dict(cardiac_disease, orient='index').stack().to_frame()
cardiac_disease = cardiac_disease.reset_index().drop('level_1', axis=1)
cardiac_disease['indicator'] = 'cardiac disease'

hypertension = pd.DataFrame.from_dict(hypertension, orient='index').stack().to_frame()
hypertension = hypertension.reset_index().drop('level_1', axis=1)
hypertension['indicator'] = 'chronic hypertension'

renal = pd.DataFrame.from_dict(renal, orient='index').stack().to_frame()
renal = renal.reset_index().drop('level_1', axis=1)
renal['indicator'] = 'RENAL disease'

autoimmune = pd.DataFrame.from_dict(autoimmune, orient='index').stack().to_frame()
autoimmune = autoimmune.reset_index().drop('level_1', axis=1)
autoimmune['indicator'] = 'autoimmune disease'

placenta_previa = pd.DataFrame.from_dict(placenta_previa, orient='index').stack().to_frame()
placenta_previa = placenta_previa.reset_index().drop('level_1', axis=1)
placenta_previa['indicator'] = 'placenta previa'

preeclampsia = pd.DataFrame.from_dict(preeclampsia, orient='index').stack().to_frame()
preeclampsia = preeclampsia.reset_index().drop('level_1', axis=1)
preeclampsia['indicator'] = 'preeclampsia'

mild_preeclampsia = pd.DataFrame.from_dict(mild_preeclampsia, orient='index').stack().to_frame()
mild_preeclampsia = mild_preeclampsia.reset_index().drop('level_1', axis=1)
mild_preeclampsia['indicator'] = 'mild preeclampsia'

substance_use = pd.DataFrame.from_dict(substance_use, orient='index').stack().to_frame()
substance_use = substance_use.reset_index().drop('level_1', axis=1)
substance_use['indicator'] = 'substance use disorder'

anemia = pd.DataFrame.from_dict(anemia, orient='index').stack().to_frame()
anemia = anemia.reset_index().drop('level_1', axis=1)
anemia['indicator'] = 'anemia'

bariatric = pd.DataFrame.from_dict(bariatric, orient='index').stack().to_frame()
bariatric = bariatric.reset_index().drop('level_1', axis=1)
bariatric['indicator'] = 'bariatric surgery'

gi_disease = pd.DataFrame.from_dict(gi_disease, orient='index').stack().to_frame()
gi_disease = gi_disease.reset_index().drop('level_1', axis=1)
gi_disease['indicator'] = 'gastrointestinal disease'

mental_health = pd.DataFrame.from_dict(mental_health, orient='index').stack().to_frame()
mental_health = mental_health.reset_index().drop('level_1', axis=1)
mental_health['indicator'] = 'mental health disorder'

neuromuscular = pd.DataFrame.from_dict(neuromuscular, orient='index').stack().to_frame()
neuromuscular = neuromuscular.reset_index().drop('level_1', axis=1)
neuromuscular['indicator'] = 'neuromuscular disease'

abruption = pd.DataFrame.from_dict(abruption, orient='index').stack().to_frame()
abruption = abruption.reset_index().drop('level_1', axis=1)
abruption['indicator'] = 'placental abruption'

accreta = pd.DataFrame.from_dict(accreta, orient='index').stack().to_frame()
accreta = accreta.reset_index().drop('level_1', axis=1)
accreta['indicator'] = 'placenta accreta spectrum'

preterm = pd.DataFrame.from_dict(preterm, orient='index').stack().to_frame()
preterm = preterm.reset_index().drop('level_1', axis=1)
preterm['indicator'] = 'preterm birth'

thyrotoxicosis = pd.DataFrame.from_dict(thyrotoxicosis, orient='index').stack().to_frame()
thyrotoxicosis = thyrotoxicosis.reset_index().drop('level_1', axis=1)
thyrotoxicosis['indicator'] = 'thyrotoxicosis'

# Fix column names
columns = ['VERSION', 'CODE', 'indicator']
gest_dm.columns = columns
hiv.columns = columns
diabetes.columns = columns
cesarean.columns = columns
pulm_ht.columns = columns
multiple_gest.columns = columns
asthma.columns = columns
bleeding.columns = columns
obesity.columns = columns
cardiac_disease.columns = columns
hypertension.columns = columns
renal.columns = columns
autoimmune.columns = columns
placenta_previa.columns = columns
preeclampsia.columns = columns
mild_preeclampsia.columns = columns
substance_use.columns = columns
anemia.columns = columns
bariatric.columns = columns
gi_disease.columns = columns
mental_health.columns = columns
neuromuscular.columns = columns
abruption.columns = columns
accreta.columns = columns
preterm.columns = columns
thyrotoxicosis.columns = columns

# Add an age category to the map
age_category = ['<35', '>=35']

# Assign weights for each condition for SMM and non-TRANSFUSION SMM
weights = {gest_dm['indicator'][0]: (1, 1),
           hiv['indicator'][0]: (30, 13),
           diabetes['indicator'][0]: (9, 6),
           cesarean['indicator'][0]: (4, 0),
           pulm_ht['indicator'][0]: (50, 32),
           multiple_gest['indicator'][0]: (20, 8),
           asthma['indicator'][0]: (11, 9),
           bleeding['indicator'][0]: (34, 23),
           obesity['indicator'][0]: (5, 4),
           cardiac_disease['indicator'][0]: (31, 22),
           hypertension['indicator'][0]: (10, 7),
           renal['indicator'][0]: (38, 26),
           autoimmune['indicator'][0]: (10, 7),
           placenta_previa['indicator'][0]: (27, 13),
           preeclampsia['indicator'][0]: (26, 16),
           mild_preeclampsia['indicator'][0]: (11, 6),
           substance_use['indicator'][0]: (10, 5),
           anemia['indicator'][0]: (20, 7),
           bariatric['indicator'][0]: (0, 0),
           gi_disease['indicator'][0]: (12, 8),
           mental_health['indicator'][0]: (7, 4),
           neuromuscular['indicator'][0]: (9, 8),
           abruption['indicator'][0]: (18, 7),
           accreta['indicator'][0]: (59, 36),
           preterm['indicator'][0]: (18, 12),
           thyrotoxicosis['indicator'][0]: (6, 0),
           age_category[1]: (2, 1)
           }

weights = pd.DataFrame.from_dict(weights, orient='index', columns=['smm score', 'non-TRANSFUSION smm score'])

# Consolidate the map
leonard_map = pd.concat([
    gest_dm,
    hiv,
    diabetes,
    cesarean,
    pulm_ht,
    multiple_gest,
    asthma,
    bleeding,
    obesity,
    cardiac_disease,
    hypertension,
    renal,
    autoimmune,
    placenta_previa,
    preeclampsia,
    mild_preeclampsia,
    substance_use,
    anemia,
    bariatric,
    gi_disease,
    mental_health,
    neuromuscular,
    abruption,
    accreta,
    preterm,
    thyrotoxicosis,
])

# Attach weights to the codes
leonard_map = leonard_map.merge(weights,
                                how='right',
                                left_on='indicator',
                                right_index=True)
