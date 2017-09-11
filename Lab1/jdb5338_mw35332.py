import matplotlib.pyplot as plt
import numpy as np
import math


#PROBLEM 1

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




#PROBLEM 2

n, p = 1, 0.5

result = []
for x in range(0, 1000):
    bernoulli = np.random.binomial(n, p, 5)
    for y in range(0, 5):
        if bernoulli[y] == 0:
            bernoulli[y] = -1
    z = float(sum(bernoulli))/5
    result.append(z)

plt.hist(result,100)
plt.title("n = 5")
plt.show()

result = []
for x in range(0, 1000):
    bernoulli = np.random.binomial(n, p, 40)
    for y in range(0, 40):
        if bernoulli[y] == 0:
            bernoulli[y] = -1
    z = float(sum(bernoulli))/5
    result.append(z)

plt.hist(result, 100)
plt.title("n = 40")
plt.show()

result = []
for x in range(0, 1000):
    bernoulli = np.random.binomial(n, p, 250)
    for y in range(0, 250):
        if bernoulli[y] == 0:
            bernoulli[y] = -1
    z = float(sum(bernoulli))/5
    result.append(z)

plt.hist(result,200)
plt.title("n = 250")
plt.show()





#PROBLEM 3

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

print(mean)
print(std)



#PROBLEM 4

mu = [-5, 5]
cov = [[20, .8],[.8, 30]]

z = np.random.multivariate_normal(mu, cov, 1000)


#Mean calculation
vector = [0, 0]
for x in range(0, 1000):
    vector[0] += z[x][0]
    vector[1] += z[x][1]
vector[0] = vector[0] / float(1000)
vector[1] = vector[1] / float(1000)

print vector
mean = vector[0] / vector[1]

#Covariance Matrix calculation

matrix = [[0,0],[0,0]]

#x11
for x in range(0, 1000):
    matrix[0][0] += (z[x][0] - vector[0]) * (z[x][0] - vector[0])

matrix[0][0] /= float(999)
#x12 & x21
for x in range(0, 1000):
    matrix[0][1] += (z[x][0] - vector[0]) * (z[x][1] - vector[1])
    matrix[1][0] += (z[x][1] - vector[1]) * (z[x][0] - vector[0])

matrix[0][1] /= float(999)
matrix[1][0] /= float(999)
#x22
for x in range(0, 1000):
    matrix[1][1] += (z[x][1] - vector[1]) * (z[x][1] - vector[1])
matrix[1][1] /= float(999)


print matrix



#PROBLEM 5

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
