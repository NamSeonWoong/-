import json
import pandas as pd
dataset = {
    'label': [],
    'content': [],
    'price': []
}

f = open('./jsondata/jsondata.json', 'r', encoding='utf-8').read()
json_data = json.loads(f)
check = 1
for line in json_data:
    labels = line['annotations']
    if len(labels) > 1:
        label_data = 1
    elif len(labels) == 0:
        label_data = 0
    else:
        label_data = 0
    text_data = line['text']
    ctt = text_data['content']
    content_data = ''
    if len(ctt) != 0:
        content_data = text_data['title'] + ctt[0]
    else:
        content_data = text_data['title']
    price_data = text_data['price']

    dataset['label'].append(label_data)
    dataset['content'].append(content_data)
    dataset['price'].append(price_data)

df = pd.DataFrame(dataset)
print(df)