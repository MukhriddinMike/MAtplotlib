import matplotlib.pyplot as plt
import numpy as np


x, y = np.loadtxt('example.txt', delimiter='.', unpack=True)
plt.plot(x, y, label='Mikeplusplus')

plt.xlabel('x')
plt.ylabel('y')
plt.title('MikePlusPlus\nAbr')
plt.legend()
plt.show()