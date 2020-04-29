import numpy as np

data = list(np.load("./article_id_list.npy", allow_pickle=True).tolist())

np.save("./article_id_list", data)