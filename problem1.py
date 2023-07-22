import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    x,y = solution(0,0)
    plt.plot(x,y)
    plt.xlabel(r"$\sf x\longrightarrow$")
    plt.ylabel(r"$\sf y\longrightarrow$")
    plt.text(1.1,0.5,r"$\frac{dy}{dx}=e^{-x}$")
    plt.grid(True)
    plt.style.use("seaborn")
    plt.show()

def solution(x_0,y_0):
    xx,yy = [],[]
    dx = 0.005
    for i in range(500):
        dydx_0 = np.e**(-x_0)
        x_0 += dx
        dy = dydx_0*dx
        y_0 += dy
        xx.append(x_0) , yy.append(y_0)
    return np.array(xx),np.array(yy)

main()