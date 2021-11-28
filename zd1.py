from numpy import *
import matplotlib.pyplot as plt
x = linspace(0, 7, 1000)
y = 5*sin(10*x)*sin(3*x)/(x**(1/2))
plt.plot(x, y)
plt.show()
