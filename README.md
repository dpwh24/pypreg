# pypreg
pypreg is a package that classifies pregnancy outcome types from health data with options to include severe maternal morbidity, adverse pregnancy outcomes, and obstetric comorbidity scores.

## Contents

## Features

This package makes available several methods to support pregnancy research:
 - [Pregnancy Outcome Classification](#pregnancy-outcome-classification):
   - Classify pregnancies by their outcome (Live birth, Stillbirth, etc.)
 - [Adverse Pregnancy Outcomes](#adverse-pregnancy-outcomes):
   - Identify the presence of indicators for Cesarean section, Preeclampsia, Gestational Diabetes, Gestational Hypertension, and Fetal Growth Restriction
 - [Severe Maternal Morbidity](#severe-maternal-morbidity):
   - Identify the presence of SMM and non-Transfusion SMM
   - Get individual flags for each of 21 indicators that make up the SMM definition
 - [Obstetric Comorbidity Index](#obstetric-comorbidity-index):
   - Get a numeric obstetric comorbidity index consistent with methods published by Bateman or Leonard

## General Usage Data Format

The methods in this package rely on diagnostic, procedure, and/or diagnostic related group (DRG) codes. These codes should be organized rowwise with the relevant patient identifiers in the context of a pandas dataframe.

## Usage

### Pregnancy Outcome Classification
A Pandas dataframe with the following elements is required to begin using this package: 

| Column       | Description                                                    | Notes                                                                                                |
|--------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Patient ID   | Unique patient identifier                                      |                                                                                                      |
| Encounter ID | Encounter identifier                                           |                                                                                                      |
| Admit date   | Date of encounter admission                                    | Date or datetime                                                                                     |
| Code type    | Describes if the given code is a procedure, diagnostic, or DRG | Accepts 'dx', 'diagnosis', 'diagnostic', 'px', 'procedure', 'drg', 'diagnostic related group'        |
| Code version | Describes the coding system of the given code                  | Accepts '9', 'ICD9', '10', 'ICD10', 'ICD10-CM', 'ICD10-PCS', 'CPT', 'CPT4', 'HCPCS', 'DRG', 'MS-DRG' |
| Code         | The procedure, diagnostic, or DRG code                         |                                                                                                      |

The dataframe may contain multiple instances of a single encounter with a variety of codes. The data should be presented 
rowwise where the codes are differentiated by the **_Code type_** and **_Code version_** columns.



### Adverse Pregnancy Outcomes

### Severe Maternal Morbidity

### Obstetric Comorbidity Index