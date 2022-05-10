import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Plot a line graph
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

# plt.plot(x, y)
# plt.title('Line Graph')
# print(plt.show())


# Create the values and a figure
x1 = np.linspace(0, 10, 100)
fig = plt.figure()

# Plot a sine and cosine wave
# plt.plot(x1, np.sin(x1), '-')
# plt.plot(x1, np.cos(x1), '--');
# print(plt.show())


# Create Subplots and configure the sine and cosine waves individually.
# plt.subplot(2,1,1) #(row_count, col_count, panel_count)
# plt.plot(x1, np.sin(x1))

# plt.subplot(2,1,2) #(row_count, col_count, panel_count)
# plt.plot(x1, np.cos(x1))

# plt.show()


