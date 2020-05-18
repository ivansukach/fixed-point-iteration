import matplotlib.pyplot as plt
import numpy as np
import math


def f(xx, yy):
    return yy / xx


# xjpo - Xj+1
# xkpo - Xk+1
def iteration(yj, h, xjpo):
    eps = 1
    yk = yj
    while eps > 0.0001:
        ykpo = yj + h * f(xjpo, yk)
        print("eps:", eps)
        eps = ykpo - yk
        yk = ykpo
    return yk


# def bdf3(p, righthandside, y0):
#


def fixed_point_iteration(amount_of_steps, h, x, y0):
    k = 1
    y = [y0]
    while k < amount_of_steps:
        y.append(iteration(y[len(y) - 1], h, x[k]))
        k += 1
    return y


fig, ax = plt.subplots()
x = np.linspace(1, 10, 91)
print("Yj+1 = ", iteration(3, 1, 2))
y = fixed_point_iteration(91, 0.1, x, 3)
print("Y[] = ", y)
print("X[] = ", x)
ax.plot(x, y)

plt.show()
