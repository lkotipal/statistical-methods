import numpy as np
from scipy.stats import f

def calculate_F(n, m, v):
	r = np.size(n)
	N = np.sum(n)
	M = np.sum(n * m) / N
	ss_b = 0
	ss_w = 0
	for j in range(r):
		ss_b = n[j] * (m[j] - M) * (m[j] - M) 
		ss_w += (n[j] - 1) * v[j]

	var_b = ss_b/(r-1)
	var_w = ss_w/(N-r)
	F = var_b / var_w

	return (F, 1 - f.cdf(F, r-1, N - r), var_w)

n      = np.array([90, 90, 90])
m_pre  = np.array([3.02, 3.12, 3.01])
v_pre  = np.array([1.54, 1.39, 1.42])
m_post = np.array([4.85, 3.72, 3.22])
v_post = np.array([0.59, 0.97, 1.21])

(F_pre, p_pre, var_pre) = calculate_F(n, m_pre, v_pre)
(F_post, p_post, var_post) = calculate_F(n, m_post, v_post)

print(f'F and p pre-test {F_pre} {p_pre}')
print(f'F and p post-test {F_post} {p_post}')

print((f.ppf(0.95, (3 - 1), (3*90 - 3))))
print(np.sqrt((3-1) * f.ppf(0.95, (3 - 1), (3*90 - 3)) * var_post * (1/30 + 1/30)))