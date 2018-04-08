import numpy as np
import pandas as pd

data = pd.read_csv('../stockprediction/01_data/data_stocks.csv')

n = data.shape[0]
p = data.shape[1]

data = data.values
snp = data[:,np.arange(0,1)]

set_size = 4
data_set = []


for idx, _ in enumerate(snp):

    row = []

    if idx + set_size > len(snp):
        break

    for v in range(set_size):
        current_index = idx + v
        current_value = snp[current_index][0]

        row.append(current_value)

    row = np.array(row)
    data_set.append(row)


data_set = np.asarray(data_set)

fmt = {'float_kind':'{:0.2f}'.format}
np.set_printoptions(suppress=True,
           formatter=fmt)

print(data_set)
np.savetxt("output.csv", data_set, delimiter=",", fmt="%10.2f")

