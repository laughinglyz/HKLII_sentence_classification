import json
import pandas as pd

# RAW_DATA_FILE = 'raw/drug_labeled_20200408.json'

# with open(RAW_DATA_FILE, 'r', encoding='UTF-8') as input_f:
#     lines = input_f.readlines()
#     count=0
#     for document_count,line in enumerate(lines):
#             data = json.loads(line)
#             for annotation in data['annotation']:
#                 for p in annotation['points']:
#                     if not p['text'].lower().islower():
#                         count+=1
#                         print(p['text'])
#     print(count)

df = pd.DataFrame([['1',2],['',1]],columns=['xiaoxin','ruoruo'])
print(df['xiaoxin'] == '')