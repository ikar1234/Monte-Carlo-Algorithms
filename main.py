import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

N = 85000  # choose accuracy, the bigger the number, the better the estimate, but the slower to compute
x = np.random.rand(N)
y = np.random.rand(N)
pi_xy = [(x[i], y[i]) for i in range(N) if sqrt(x[i] ** 2 + y[i] ** 2) <= 1]

print(4 * len(pi_xy) / len(x)) # gives us an estmate of pi

""" If you want to plot the points in the circle
pi_x = [x[0] for x in pi_xy]
pi_y = [x[1] for x in pi_xy]
plt.scatter(pi_x, pi_y)
plt.show()
"""
