import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Histogram
data1 = np.random.randn(100)
# plt.hist(data1)
# plt.title('Histogram')
# plt.show()


# Bar Chart
data2 = [5. , 25. , 50. , 20.]
# plt.bar(range(len(data2)), data2)
# plt.title('Bar Chart')
# plt.show()


# Horizontal Bar Chart
# plt.barh(range(len(data2)), data2)
# plt.title('Horizontal Bar Chart')
# plt.show() 


# Stacked Bar Chart
a = [15., 30., 45., 22.]
b = [15., 25., 50., 20.]
z1 = range(4)

plt.bar(z1, a, color = 'b')
plt.bar(z1, b, color = 'r', bottom = a)
plt.title('Stacked Bar Chart')
plt.show()
