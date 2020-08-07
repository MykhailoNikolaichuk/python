import random
import numpy as np
import matplotlib.pyplot as plt



accuracy = 3000
dots_in_circle = 0
dots_total = 0
for i in range(accuracy):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = x*x + y*y
    if distance <= 1:
        color = 'red'
        dots_in_circle += 1
    else:
        color = 'black'
    dots_total +=1

    plt.scatter(x, y, s = 2, c = color)


pi = (dots_in_circle * 4) / dots_total
plt.xlabel(f'We got PI equal to = [{pi}] with {accuracy} dots used')
plt.title('We counting Pi here, no jokes')
plt.axes().set_aspect('equal', 'datalim')
plt.show()
