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

## Pregnancy Outcome Classification
This module is an implementation of the obstetric classification algorithm given by Moll(2020).

### Data Requirements
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

### Code selection

#### Crosswalk
The codes given by Moll(2020) are primarily in the ICD10 coding system and are crosswalked to ICD9 for broader use.
Crosswalked codes are retrieved via General Equivalence Mappings. ICD10 codes are mapped back to ICD9, and ICD9 codes
are mapped forward to ICD10. The resulting codes are reviewed and kept if they are related to an obstetric outcome, and,
if the original ICD10 code broadly refers to labor and delivery, then the mapped codes may also. 

#### Change to Moll codes
ICD10 procedure codes 10D17ZZ and 10D18ZZ refer to extraction of retained products of conception. These codes describe
a dilation and curettage procedure which is more frequently, though not exclusively, performed on abortive outcomes. 
These codes lead to misclassification of abortive outcomes as unknown deliveries and were removed from this 
implementation.

#### Expanded codes
Expanded codes are added based upon a review of ICD9 and ICD10 codes for other obstetric outcomes not captured.
This primarily captures codes where episode of care indicates _delivered_ in ICD9.

### Algorithm
The specifics of the algorithm are contained within Moll(2020). In short, each code provided is classified by regular 
expression matching. Each individual patient is then processed independently to prioritize certain outcomes. The 
outcomes are then checked to ensure that the spacing between different pregnancy outcome types is sensible. Outcome 
types that do not fit the spacing are dropped from consideration. A pregnancy start window is estimated based on the 
outcome type. The start of this window is then adjusted if needed so that it is not overlapping a previous pregnancy.

### Usage

Four processes are exposed and available to be imported:

1. `process_outcomes`
  - the entry into the classifcation algorithm. All parameters are required except for the `expanded` 
flag which indicates if you would like to use the Moll codes or an expanded list of codes identified by this author
  - the dataframe need not have the columns in a standardized order, instead the required column names must be passed 
as strings

```python
from pypreg import process_outcomes

process_outcomes(df: pd.DataFrame,
                 patient_col: str,
                 encounter_col: str,
                 admit_date_col: str,
                 version_col: str,
                 type_col: str,
                 code_col: str,
                 expanded: bool = False)
```
#### Output
This process will produce a pandas dataframe with the following data (column names that are reflexive of provided data 
will use the originally provided column name): 


| Column       |Description|Notes|
|--------------|----|----|
| Patient ID   |Unique patient identifier|Will be the same as originally provided|
| Preg_num     |Pregnancy identifier per patient|Synonomous with gravida, but only relevant to the provided data (uncaptured pregnancies cannot be counted)|
| Encounter ID |Encounter identifier belonging to the outcome encounter|Will be the same as originally provided|
| Admit        |Date of admission for the outcome encounter|Formatted as date, not datetime||
|Event_date|Date of admission for the outcome encounter|Formatted as date, not datetime||
|Outcome|String classification of the pregnancy outcome| live_birth, stillbirth, delivery, trophoblastic, ectopic, therapeutic_abortion, spontaneous_abortion|
|Start_window|Date that delineates the beginning of the pregnancy start window||
|End_window|Date that delineates the end of the pregnancy start window||

2. `OUTCOME_LIST`
  - exports the list of pregnancy outcomes in hierarchical order
```python
from pypreg import OUTCOME_LIST

print(OUTCOME_LIST)
['LIVE_BIRTH', 'STILLBIRTH', 'DELIVERY', 'TROPHOBLASTIC', 'ECTOPIC', 'THERAPEUTIC_ABORTION', 'SPONTANEOUS_ABORTION']
```
3. `OUTCOMES`
  - exports the full list of codes, the code type, the code version, and the association outcome classification
  - codes are given as a regular expression
```python
from pypreg import OUTCOMES

print(OUTCOMES.head())
  code_type version     schema                      code  outcome
0        DX   ICD10       MOLL                 ^O0[08].*  ECTOPIC
1        DX    ICD9  CROSSWALK                    ^633.*  ECTOPIC
2        PX   ICD10       MOLL  ^10(D2[78]|T2[03478])ZZ$  ECTOPIC
3        PX    ICD9  CROSSWALK                     ^743$  ECTOPIC
4        PX    ICD9  CROSSWALK                 ^66[06]2$  ECTOPIC

```
4. `map_version_split`
  - splits `OUTCOMES` into 4 subcategories
    - ICD9 Diagnostic codes
    - ICD10 Diagnositc codes
    - Procedure codes
    - Diagnostic Related Group (DRG) codes
  - default behavior is to not include the expanded code list
```python
from pypreg import map_version_split

map_version_split(expanded: bool = False)
```

### Adverse Pregnancy Outcomes

### Severe Maternal Morbidity

### Obstetric Comorbidity Index