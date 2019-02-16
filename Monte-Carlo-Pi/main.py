import numpy as np
import time
from math import pi

def monte_carlo(acc):
    t = time.time()

    x = np.random.rand(acc)  # array of random numbers from 0 to the estimate
    y = np.random.rand(acc)

    distances = x ** 2 + y**2       # creates an array of distances to (0;0) for each point
    pi_xy = np.column_stack((x, y))  # numpy way of creating an array of (x;y) coordinates
    pi_xy = pi_xy[distances <= 1]  # filters pi_xy using distances inferior to 1

    """ If you want to plot the points in the circle
    import matplotlib.pyplot as plt
    pi_x = pi_xy[ : ,0]
    pi_y = pi_xy[ : ,1]  
    plt.scatter(pi_x, pi_y)
    plt.show()
    """
    return (time.time() - t), (4 * len(pi_xy) / acc) # returns compilation time and estimated value


N = 10**7  # choose accuracy 
a = np.array([[monte_carlo(N)[0],monte_carlo(N)[1]] for x in range(350)])
print(sum(a[:,0])/len(a[:,0]))  # average run-time -> ~1.17642 with 350 and ~0.82731 with 3 tries
print(sum(a[:,1])/len(a[:,1]))  # average estimation -> 3.1415935862857154 with 350 tries!
print(sorted([(x,abs(x-pi)) for x in a[:,1]],key=lambda x: x[0])[0]) # finds the best estimation and the difference with pi
  
