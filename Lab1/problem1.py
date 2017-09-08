import matplotlib.pyplot as plt
import numpy as np
import math

mu1 = -10
mu2 = 10
variance1 = 25
sigma = math.sqrt(variance1)
dis1 = np.random.normal(mu1, sigma, 1000)
dis2 = np.random.normal(mu2, sigma, 1000)
dis3 = dis1 + dis2

mu3 = np.mean(dis3)
sig3 = np.std(dis3)

plt.hist(dis3, 100)

plt.show()