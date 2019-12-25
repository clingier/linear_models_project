import pandas as pd
import numpy as np

#Importing Data
df = pd.read_excel('clinical_dataset.xlsx', sheet_name=1)

df_outcome_data = pd.read_excel('clinical_dataset.xlsx', sheet_name=3)

#Add the interesting columns

df['survstat'] = df_outcome_data['sstat']
df['rfs'] = df_outcome_data['RFS']
df['rfs_ind'] = df_outcome_data['rfs_ind']
df['rcb'] = df_outcome_data['RCBClass']

#Encode ordinal columns

## cancer laterality encoding
df['right'] = np.where(df.Laterality == 2, 1, 0)
df['right'] = np.where(df.Laterality == 1, 1, 0)


## race encoding
df['caucasian'] = np.where(df.race_id == 1, 1, 0)
df['af_american'] = np.where(df.race_id == 3, 1, 0)
df['asian'] = np.where(df.race_id == 4, 1, 0)
df['pac_islander'] = np.where(df.race_id == 5, 1, 0)
# df['alaskan'] = np.where(df.race_id == 6, 1, 0)

## genes combination encoding
df['hr_p_her2_neg'] = np.where(df.HR_HER2_CATEGORY == 1, 1, 0)
df['her2_pos'] = np.where(df.HR_HER2_CATEGORY == 2, 1, 0)
df['triple_neg'] = np.where(df.HR_HER2_CATEGORY == 3, 1, 0)

#Rename the columns

df.rename(
    columns={  
        'ERpos':'er', 
        'PgRpos':'pr',
        'HR Pos': 'hr',
        'HR_HER2_CATEGORY' : 'hr_her_cat',
        'MRI LD Baseline' : 'mri_baseline',
        'MRI LD 1-3dAC' : 'mri_dac',
        'MRI LD InterReg' : 'mri_interreg',
        'MRI LD PreSurg' : 'mri_presurg',
        'BilateralCa': 'bilateral',
        'Her2MostPos' : 'her2'
    },
    inplace=True
)

df.drop(['DataExtractDt', 'Laterality', 'SUBJECTID', 'HR_HER2_STATUS'], 
    axis=1,
    inplace=True)

df.drop(['caucasian', 'af_american', 'pac_islander', 'asian'], axis=1, inplace=True)

df['hr_not_er'] = df['hr'] - df['er']

df.drop('hr', axis=1, inplace=True)

df.dropna(inplace=True)

df.to_csv('clean_data.csv')