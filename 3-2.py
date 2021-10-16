import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

X0 = 0
Y0 = 3

rng = np.random.default_rng(250198)
r = rng.uniform(size=25000)
x = np.linspace(-25, 25, int(1E6))

X = Y0 * np.tan(np.pi * r - np.pi/2) + X0

plt.hist(X, bins = 100, range = (-50, 50), density=True, label=r'$X(r)$')
plt.legend()
plt.show()

plt.hist(X, bins = 100, range = (-25, 25), density=True, label=r'$X(r)$')
plt.plot(x, norm.pdf(x, 0, 6/2.355), label=r'$N(0, \frac{6}{2.355})$')
plt.legend()
plt.show()