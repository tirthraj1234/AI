import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

print(type(numbers))# type n dimensional array

print(numbers.shape)# there are 5 elements in one dimensional array

print(numbers.ndim)# number of dimension 

print(numbers.size)# array size

print(numbers.dtype)# array data type

#indexing
print(numbers[0])
print(numbers[2])
print(numbers[-1])

#slicing
print(numbers[1:4])

#mathematical operator
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

#statistical functions
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.sum(a))

#Reshape
array = np.array([1, 2, 3, 4, 5, 6])

matrix = array.reshape(2, 3)# give a matrix of 2 into 3

print(matrix)

