
# Source: https://www.hackertrail.com/talent/backend/numpy-interview-questions-answers/

# NumPy(Numerical Python) is an open-source library of Python. It is designed to perform complex mathematical, image processing, 
# quantum computing, and statistical operations, etc., on matrices and multidimensional arrays. 
# The NumPy N-dimensional arrays are used to perform indexing, slicing, splitting, joining, reshaping, 
# and other complex manipulations. 


# 1. Name a few use cases where NumPy is useful. 
# To perform complex mathematical computations on arrays 
# To use multi-dimensional arrays and matrices in operations
# To execute trigonometric, statistical, and algebraic functions 
# To execute transforms and methods for shape manipulation 
# To generate random numbers 
# To add/ delete/ sort/ split arrays 

# 2. How many dimensions can a NumPy array have? 
# In NumPy, an array can have N-dimensions, and is called a ndarray. 
# Ndarray is a multidimensional container which contains elements of the same type and size. 
# The number of dimensions in a ndarray is also known as ‘rank’. 
# A tuple of integers called ‘shape’ defines the size of the array in each dimension. 
# The data type of elements in ndarray is defined by a  ‘dtype’ object. 

from re import A
import numpy as np


# Create a Numpy Array
array = np.arange(20)
print(array)


# 1-D Numpy Addition
array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])
array_add = array1 + array2
print(array_add)


# 1-D Numpy Subtraction
array_subtract = array2 - array1
print(array_subtract)


# 1-D Numpy Multiplication
array_multiply = array1 * array2
print(array_multiply) #result: [ 6 14 24 36 50]


# 1-D Numpy Division
array_divide = array1 / array2
print(array_divide) #result: [0.16666667  0.28571429  0.375  0.44444444  0.5  ]


# 1-D Numpy Powers
array_squared = array1 **2
array_cubed = np.power(array1,3)
print(array_squared) #result: [ 1  4  9 16 25]
print(array_cubed) #result: [  1   8  27  64 125]


# 1-D Numpy Conditional Expressions (Compare arrays using conditions)
array_cond = array2 >= 3
print(array_cond) #result: [ True  True  True  True  True]



# 2-D Numpy Addition
a = np.array([[3,2], [1,0]]) 
b = np.array([[2,5], [3,4]])
array2d_add = a + b
print(array2d_add) #result: [[5 7], [4 4]]

# 2-D Numpy Subtraction
array2d_subtract = b - a
print(array2d_subtract) #result: [[-1  3], [ 2  4]]

# 2-D Numpy Multiplication
array2d_multiply = a * b
print(array2d_multiply) #result: [[ 6 10], [ 3  0]]

# 2-D Numpy Division
array2d_divide = b / a
print(array2d_divide) #result: [[0.66666667  2.5], [3.  inf]]


# 2-D Numpy Matrix Multiplication (rows of A x columns of B)
array_matrix_multiply = a @ b
print(array_matrix_multiply)


# Shape of a Numpy Array: (Returns the shape of the array in number of rows and columns)
array_sh = np.array([[3,2,1], [6,5,4]])
print(array_sh.shape) #result: (2, 3)


# Slicing in Numpy
# The basic slice syntax is i:j:k where i is the starting index, j is the stopping index, and k is the step (k≠0)

# 1-D Array Slicing
array_slice_1d = np.array([1,2,3,4,5,6,7,8,9])
slice1 = array_slice_1d[1::3]
print(slice1) #result:[2 5 8]


# 2-D Array Slicing (first select rows and then the columns)
array_slice_2d  = np.array([[10, 11, 12, 13, 14], 
                            [15, 16, 17, 18, 19], 
                            [20, 21, 22, 23, 24], 
                            [25, 26, 27, 28, 29]])
slice2 = array_slice_2d[1:4, 2:4]
print(slice2) #result: [[17 18]
#                         [22 23]
#                         [27 28]]


# 3-D Array Slicing
array_slice_3d = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
                            [[20, 21, 22], [23, 24, 25], [26, 27, 28]], 
                            [[30, 31, 32], [33, 34, 35], [36, 37, 38]]]) 
slice3 = array_slice_3d[:2, 1:, :2]
print(slice3) #result: [[[13 14]
#                         [16 17]]
#                       
#                         [[23 24]
#                         [26 27]]]
