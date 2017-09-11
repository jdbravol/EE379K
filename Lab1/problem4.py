import matplotlib.pyplot as plt
import numpy as np
import math

mu = [-5, 5]
cov = [[20, .8],[.8, 30]]

z = np.random.multivariate_normal(mu,cov, 1000)


#Mean calculation
mu = [0, 0]
for x in range(0, 1000):
    mu[0] += z[x][0]
    mu[1] += z[x][1]
mu[0] = mu[0]/float(1000)
mu[1] = mu[1]/float(1000)

mean = mu[0]/mu[1]

#Covariance Matrix calculation

matrix = [[0,0],[0,0]]

#x11
for x in range(0, 1000):
    matrix[0][0] += (z[x][0] - mu[0])*(z[x][0] - mu[0])

matrix[0][0] /= float(999)
#x12 & x21
for x in range(0, 1000):
    matrix[0][1] += (z[x][0] - mu[0])*(z[x][1] - mu[1])
    matrix[1][0] += (z[x][1] - mu[1])*(z[x][0] - mu[0])

matrix[0][1] /= float(999)
matrix[1][0] /= float(999)
#x22
for x in range(0, 1000):
    matrix[1][1] += (z[x][1] - mu[1])*(z[x][1] - mu[1])
matrix[1][1] /= float(999)


print matrix