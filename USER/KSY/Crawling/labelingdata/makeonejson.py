import json

temp0 = []
for line in open("file0.json", "r", encoding="utf-8"):
    temp0.append(json.loads(line))

temp1 = []
for line in open("file1.json", "r", encoding="utf-8"):
    temp1.append(json.loads(line))

temp2 = []
for line in open("file2.json", "r", encoding="utf-8"):
    temp2.append(json.loads(line))

temp3 = []
for line in open("file3.json", "r", encoding="utf-8"):
    temp3.append(json.loads(line))

temp4 = []
for line in open("file4.json", "r", encoding="utf-8"):
    temp4.append(json.loads(line))

temp = temp1 + temp2 + temp3 + temp4

with open("./data.json", "w", encoding="utf-8") as f:
    json.dump(temp, f, indent="\t")