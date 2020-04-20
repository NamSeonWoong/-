import numpy as np
import csv

data = np.load("./process_datas.npy", allow_pickle=True).tolist()

csvfile = open("./data.csv", "w", encoding="utf-8")

csvwriter = csv.writer(csvfile)
for row in data:
    one = [row["title"], row["category"], row["price"], row["content"], row["date"], row["url"]]
    csvwriter.writerow(one)

csvfile.close()