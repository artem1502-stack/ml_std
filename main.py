import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi/2, np.pi/2, 1000)
y = np.sin(x)


plt.plot(x, y)


plt.show()
