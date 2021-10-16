import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest
from scipy.stats import pearsonr

#a = pow(7, 5)
#m = pow(2, 31) - 1
a = 40692
m = 2147483399

X = np.zeros(10000)

#X[0] = int(int(time()) % m)
X[0] = 250198

for i in range(1, X.size):
	X[i] = int(a * X[i-1] % m)

plt.hist(X/m, density=True)
plt.show()

#rng = np.random.default_rng()
#r = rng.uniform(size=1000000)

print(kstest(X/m, 'uniform'))
#print(kstest(r, 'uniform'))

print(pearsonr(X[:-1]/m, X[1:]/m))
#print(pearsonr(r[:-1], r[1:]))