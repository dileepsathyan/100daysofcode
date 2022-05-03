import numpy as np

# Create a Numpy array in a particular sequence with the starting and ending numbers.
arange1 = np.arange(1,30,4)
# print(arange1) #result: [ 1  5  9 13 17 21 25 29]


# Create a 1-D array of Zeros
zeros_1d = np.zeros(3)
#print(zeros_1d) #result: [0. 0. 0.]


# Create a 2-D array of Zeros
zeros_2d = np.zeros((3, 4))
# print(zeros_2d) #result: [[0. 0. 0. 0.]
#                           [0. 0. 0. 0.]
#                           [0. 0. 0. 0.]]


# Similarly arrays of 1s in 1-D
ones_1d = np.ones(2)
# print(ones_1d) #result: [1. 1.]


# Similarly arrays of 1s in 2-D
ones_2d = np.ones((2, 3))
# print(ones_2d) #result: [[1. 1. 1.]
#                         [1. 1. 1.]]


# The 'empty' function creates an array. Its initial content is random and depends on the state of the memory.
empty_1d = np.empty(2)
# print(empty_1d) #result: [-5.73021895e-300  8.04338871e-320]

empty_2d = np.empty((2,4))
# print(empty_2d) #result: [[0.e+000 8.e-323 0.e+000 0.e+000]
#                           [0.e+000 0.e+000 0.e+000 0.e+000]]



# The 'full' function creates a n * n array filled with the given value.
full_2d = np.full((2,3), 4.15)
# print(full_2d) #result: [[4.15 4.15 4.15]
#                          [4.15 4.15 4.15]]


# The 'eye' function creates an n * n matrix with the diagonal 1s and the others 0
eye2d = np.eye(3,3)
# print(eye2d) #result: [[1. 0. 0.]
#                        [0. 1. 0.]
#                        [0. 0. 1.]]



# The function 'linspace' returns evenly spaced numbers over a specified interval. 
# For example, the below function returns four equally spaced numbers between the interval 0 and 10.
linspace_1d = np.linspace(0,10,4)
# print(linspace_1d) #result: [0.  3.33333333  6.66666667  10.  ]


# To create a 2-D array, pass a sequence of lists to the array function.
arr_2d = np.array([(2,3,4), (5,6,7)])
# print(arr_2d) #result: [[2 3 4]
#                         [5 6 7]]



# Use 'random' function to create an array filled with random values between 0 and 1. 
# This is particularly useful for problems where a random state is needed to get started.
rand_2d = np.random.random((2,3))
# print(rand_2d) #result: [[0.05094358 0.99163629 0.19804949]
#                          [0.2024887  0.64018522 0.03417031]