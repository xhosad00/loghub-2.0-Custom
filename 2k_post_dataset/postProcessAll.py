import os
from pathlib import Path
import pandas as pd
from post_process import correct_single_template 

BASE_DIR = Path('./')

def postProcessDataset(dataset:str):
    def adjustEventTemplate(pathToFile:Path):
        df = pd.read_csv(pathToFile, dtype=str)
        df['EventTemplate'] = df['EventTemplate'].apply(
            lambda et: correct_single_template(et)
        )
        df.to_csv(pathToFile, index=False) #allready indexd
        print(f'Updated {pathToFile.name}')

    datasetDir = BASE_DIR / dataset
    pathStructured:Path     = datasetDir / f'{dataset}_2K.log_structured.csv'
    pathStructuredCor:Path  = datasetDir / f'{dataset}_2K.log_structured_corrected.csv'
    pathTemplates:Path      = datasetDir / f'{dataset}_2K.log_templates.csv'
    pathTemplatesCor:Path   = datasetDir / f'{dataset}_2K.log_templates_corrected.csv'

    # if not pathStructured.is_file() or not pathTemplates.is_file():
    #     print(f'Did not find files {pathStructured} and {pathTemplates}')
    #     return
    if not pathTemplates.is_file():
        print(f'Did not find file {pathTemplates}')
        return
    #Corrected
    adjustEventTemplate(pathStructured)
    adjustEventTemplate(pathStructuredCor)
    #Templates
    adjustEventTemplate(pathTemplates)
    adjustEventTemplate(pathTemplatesCor)

datasets_2k = [
   'Apache',
   'BGL',
   'HDFS',
   'HPC',
   'Hadoop',
   'HealthApp',
   'Linux',
   'Mac',
   'OpenSSH',
   'OpenStack',
   'Proxifier',
   'Spark',
   'Thunderbird',
   'Zookeeper',
]

if __name__ == "__main__":
    for dataset in datasets_2k:
        postProcessDataset(dataset)