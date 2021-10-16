import numpy as np
import matplotlib.pyplot as plt

a = np.transpose(np.loadtxt("train_sample21_class_a.txt"))
b = np.transpose(np.loadtxt("train_sample21_class_b.txt"))

plt.plot(a[0], a[1], '.')
plt.plot(b[0], b[1], '.')
plt.show()

V_a = np.cov(a)
V_b = np.cov(b)
mu_a = np.mean(a, axis=1)
mu_b = np.mean(b, axis=1)

c = np.linalg.inv(V_a + V_b).dot(mu_a - mu_b)
print(c)
x_a = np.transpose(a).dot(c)
x_b = np.transpose(b).dot(c)

plt.hist(x_a, alpha=0.5)
plt.hist(x_b, alpha=0.5)
plt.show()

cutoff = np.percentile(x_a, 10)
print(np.sum(x_b < cutoff)/np.size(x_b) * 100)

plt.plot(a[0, x_a < cutoff], a[1, x_a < cutoff], '.')
plt.plot(b[0, x_b < cutoff], b[1, x_b < cutoff], '.')
plt.show()