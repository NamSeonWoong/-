import numpy as np

data = np.load("./article_id_list.npy", allow_pickle=True).tolist()
print(list(data))