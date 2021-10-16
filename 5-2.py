import numpy as np
from scipy.stats import kstwobign
from math import sqrt

A = np.array([81, 82, 87, 93, 102, 104, 108, 112, 116, 122, 125, 131, 131, 133, 134, 139, 139, 142, 144, 146, 152, 156, 182, 202, 206, 216, 226, 270])
B = np.array([8, 12, 14, 16, 22, 26, 26, 50, 64, 68, 76, 79, 83, 88, 96, 97, 98, 99, 103, 105, 107, 113, 114, 115, 126, 128, 130, 132, 138, 150, 169, 171])

F_A = np.array([(A < i).sum() for i in range(300)])/np.size(A)
F_B = np.array([(B < i).sum() for i in range(300)])/np.size(B)

diff_max = np.abs(F_A - F_B).max()
print(diff_max)

P_ks = 1 - kstwobign.cdf(diff_max * sqrt(np.size(A) * np.size(B) / (np.size(A) + np.size(B))))
print(P_ks)