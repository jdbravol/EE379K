import numpy as np
import pandas as pd

file = pd.read_csv("./PatientData.csv", header=None, index_col=None)
print(file.shape)
file.reindex(range(453))

for y in range(0, file.shape[1]):
    avg = []
    for x in range(0, file.shape[0]):
        if file[y][x] != '?':
            avg.append(file[y][x])
    avg = np.array(avg).astype(np.float)
    average = np.mean(avg)
    for z in range(0, file.shape[0]):
        if file[y][z] == '?':
            file[y][z] = average

file.to_csv("./PatientData.csv")
