import pandas as pd

data = pd.read_csv('./file.csv', encoding='utf-8')
print(data[:5])
del data['annotation_approver']
del data['id']
del data['user']
data['label'] = data['label'].replace([])