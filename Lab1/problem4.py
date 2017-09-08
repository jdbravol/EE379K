import matplotlib.pyplot as plt
import numpy as np
import math

mu = [-5, 5]
cov = [[20, .8],[.8, 30]]

z = np.random.multivariate_normal(mu,cov, 3)


#Mean calculation
mu1 = 0
mu2 = 0
for x in range(0, 3):
    mu1 += z[x][0]
    mu2 += z[x][1]
mu1 = mu1/float(3)
mu2 = mu2/float(3)

mean = mu1/mu2

#Covariance calculation

sum = 0
for x in range(0, 1000):
    sum += (z[x][0] - mu1)*(z[x][1] - mu2)


cov = 1/1000*()
