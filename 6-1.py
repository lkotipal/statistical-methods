import numpy as np
from scipy.stats import chisquare

# Classes are the same in each file
real = np.loadtxt("real_mass.dat")[:,2]
MC1 = np.loadtxt("MC1_mass.dat")[:,2]
MC2 = np.loadtxt("MC2_mass.dat")[:,2]

print(chisquare(real, MC1))
print(chisquare(real, MC2))

[a_min, min] = [0, chisquare(real, MC2).statistic]
for a in np.linspace(0, 1, 10001):
	x = chisquare(real, a * MC1 + (1 - a) * MC2).statistic
	if x < min:
		[a_min, min] = [a, x]

print(f'Optimal a {a_min} with chi-square statistic of {min}')