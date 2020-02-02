import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 1
N = math.sqrt(variance)
x = np.linspace(mu - 90*N, mu + 90*N, 1000)
plt.plot(x, stats.norm.pdf(x, mu, N))
plt.title('F(N,S; N=90)')
plt.xlabel('X')
plt.ylabel('F(N,S)')
plt.show()
