import numpy as np
import matplotlib.pyplot as plt


def batman(x,y):
    return (3*np.sqrt(abs(4-(np.abs(x)-2)**2)) +np.abs(x)-20-4*y)*(3*np.sqrt(abs((4-(np.abs(x)-6)**2)))+np.abs(x)-20-4*y)*(x**2 + 4*y**2-100*np.sqrt(abs((np.abs((7-np.abs(2*y-1))) / (7-np.abs(2*y-1))))))*(2*(np.abs(x)-3)**2-9*y + 18*np.sqrt(abs((np.abs((2-np.abs((np.abs(x)-4)))) / (2-np.abs((np.abs(x)-4)))))))*((-68)*np.abs((np.abs(x)-3 / 2))-9*y + 54*np.sqrt(abs((np.abs((43-np.abs((136*np.abs(x)-229)))) / (43-np.abs((136*np.abs(x)-229)))))))*(y-5*np.sqrt(abs((np.abs((1-np.abs(x))) /(1-np.abs(x))))))


def monte_carlo(acc):

    x = np.random.uniform(low=-10, high=10, size=(acc,))
    y = np.random.uniform(low=-5, high=5, size=(acc,))

    distances = batman(x, y)
    pi_xy = np.column_stack((x, y))  # numpy way of creating an array of (x;y) coordinates
    pi_xy = pi_xy[distances<=0.6]
    x1 = pi_xy[:,0]
    # print(pi_xy[:,0])
    y1 = pi_xy[:,1]
    ellipse = (x1 / 7) ** 2 + (y1 / 3) ** 2
    distances2 = batman(x1,y1)
    pi_xy = pi_xy[ellipse <= 3]
    pi_xy = pi_xy[pi_xy.sum(-1)<11]
    pi_xy = pi_xy[pi_xy.sum(-1)>-11]

    return pi_xy[:,0], pi_xy[:,1]


def main():
    n1 = 500
    n2=10**3
    n3=10**4
    n4=10**5
    monte1 = monte_carlo(n1)
    monte2 = monte_carlo(n2)
    monte3 = monte_carlo(n3)
    monte4 = monte_carlo(n4)
    fig, axes = plt.subplots(1, 4, figsize=(12,3))

    axes[0].scatter(monte1[0], monte1[1],s=0.3,color="g")
    axes[0].set_xlim([-12,12])
    axes[0].set_ylim([-12, 12])
    axes[0].set_title(f"${n1}$"+" points")

    axes[1].scatter(monte2[0], monte2[1],s=0.3,color="r")
    axes[1].set_xlim([-12,12])
    axes[1].set_ylim([-12, 12])
    axes[1].set_title(f"${n2}$")

    axes[2].scatter(monte3[0], monte3[1],s=0.3,color="b")
    axes[2].set_xlim([-12,12])
    axes[2].set_ylim([-12, 12])
    axes[2].set_title(f"${n3}$")

    axes[3].scatter(monte4[0], monte4[1],s=0.3,color="g")
    axes[3].set_xlim([-12,12])
    axes[3].set_ylim([-12, 12])
    axes[3].set_title(f"${n4}$")

    plt.show()


main()
