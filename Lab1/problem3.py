import numpy as np
import math

mu = 0
sigma = 5

x = np.random.normal(mu,sigma,25000)

sum = 0
for i in range(0, 25000):
    sum += x[i]
mean = sum / float(25000)

sum = 0
for j in range(0, 25000):
    sum += math.pow(x[j] - mean, 2)

std = math.sqrt((1/float(25000))*sum)

print mean
print std