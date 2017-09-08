import matplotlib.pyplot as plt
import numpy as np

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