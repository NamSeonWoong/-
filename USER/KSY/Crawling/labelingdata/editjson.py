import json

with open("./data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
# print(data[121]['text'])

for one in data:
    one['text'] = eval(one['text'])

# print(data[121]['text']['title'])

with open("./jsondata.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent="\t")
