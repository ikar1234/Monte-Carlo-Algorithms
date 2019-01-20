import matplotlib.pyplot as plt
import numpy as np


# print(sum(l)/len(l))
N = 8500
x = np.random.rand(N)
y = np.random.rand(N)
pi_xy = [(x[i], y[i]) for i in range(N) if x[i] ** 2 + y[i] ** 2 <= 1]
pi_x = [x[0] for x in pi_xy]
pi_y = [x[1] for x in pi_xy]
plt.scatter(pi_x, pi_y)
plt.show()
print(4 * len(pi_xy) / len(x))