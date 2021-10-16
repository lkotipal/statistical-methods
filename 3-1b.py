import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import kstest

rng = np.random.default_rng(250198)
r = rng.uniform(size=[1000, 12])
x = np.linspace(0, 12, int(1E6))

plt.hist(r.sum(axis=1), range = (0, 12), bins=48, density=True, label='Sums')
plt.plot(x, norm.pdf(x, 6, 1/np.sqrt(2)), label=r'$N(6, 1/\sqrt{2})$')
plt.show()