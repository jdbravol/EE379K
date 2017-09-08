import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

file = pd.read_csv('./PatientData.csv')
file.shape


for y in range (0, file.shape[1]):
	avg = []
	for x in range (0, file.shape[0]):
		if (file.loc[x,y] != "?"):
			avg.concat(file.loc[x,y])
	average = math.mean(avg)
	for z in range (0, file.shape[0]):
		if file.loc[z,y] == "?":
			file.loc[z,y] = average


	

