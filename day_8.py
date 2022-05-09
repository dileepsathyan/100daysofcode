from turtle import color, title
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.array(["a", "b", "c", "d", "e"])
y = np.array([24, 85, 47, 38, 62])


# Plot a Simple Vertical Bar Chart
plt.bar(x, y)
plt.title('Bar Chart')
plt.show()


# Plot a Horizontal Bar Chart
plt.barh(x, y)
plt.title('Horizontal Bar Chart')
plt.show()


# Plot a Horizontal Bar Chart in a specified color
plt.barh(x, y, color= 'y')
plt.title('Horizontal Bar Chart')
plt.show()


# Plot a Simple Vertical Bar Chart with explicit column widths
plt.bar(x, y, color='orange', width=.2)
plt.title('Bar Chart')
plt.show()


# Plot a Horizontal Bar Chart in a specified color & explicit bar heights
plt.barh(x, y, color= 'y', height=.2)
plt.title('Horizontal Bar Chart')
plt.show()


# Create a Pie Chart
# plt.pie(y, labels=x)
# plt.title('Pie Chart')
# plt.show()


# Create a Pie Chart with exploded view
# plt.pie(y, labels=x, explode=[0.2, 0, 0, 0, 0])
# plt.title('Pie Chart')
# plt.show()


# Create a Pie Chart with exploded view & with shadow and legend
plt.pie(y, labels=x, explode=[0.2, 0, 0, 0, 0], shadow=True)
plt.legend()
plt.title('Pie Chart')
plt.show()

