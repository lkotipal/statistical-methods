import matplotlib.pyplot as plt
import numpy as np

A = 20
h = 2.40
l = np.linspace(2, 10, 1000)
w = A / l

rho = h * np.sqrt(l**2 + w**2) / np.sqrt((l + w)**2 + 2 * h**2)

plt.plot(l, rho, label='paska')
plt.axvline(x=np.sqrt(20), c='red', ls='--')
plt.show()