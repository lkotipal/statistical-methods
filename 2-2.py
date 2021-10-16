import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import poisson
from math import sqrt

x = np.arange(0, 13, 1)
plt.bar(x, poisson.pmf(x, 6), 1, alpha=0.5, label='Poisson')
plt.bar(x, norm.pdf(x, 6, sqrt(6)), 1, alpha=0.5, label='Gaussian')
plt.legend()
plt.show()

plt.bar(x, binom.pmf(x, 12, 0.5), 1, alpha=0.5, label='Binomial')
plt.bar(x, norm.pdf(x, 6, sqrt(6)), 1, alpha=0.5, label='Gaussian')
plt.legend()
plt.show()

plt.bar(x, binom.pmf(x, 1200, 0.005), 1, alpha=0.5, label='Binomial')
plt.bar(x, norm.pdf(x, 6, sqrt(6)), 1, alpha=0.5, label='Gaussian')
plt.legend()
plt.show()

plt.bar(x, binom.pmf(x, 12, 0.5), 1, alpha=0.5, label='Binomial')
plt.bar(x, poisson.pmf(x, 6), 1, alpha=0.5, label='Poisson')
plt.legend()
plt.show()

plt.bar(x, binom.pmf(x, 1200, 0.005), 1, alpha=0.5, label='Binomial')
plt.bar(x, poisson.pmf(x, 6), 1, alpha=0.5, label='Poisson')
plt.legend()
plt.show()