import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
print(x)
y = np.random.rand(N)

plt.scatter(x, y)
plt.show()