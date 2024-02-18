import numpy as np
from numpy.random import random 

import matplotlib.pyplot as plt
#from scipy import misc #contains an image 
from PIL import Image # for reading Image files


# 1 Dimension array

my_array = np.array([1.1, 9.2, 8.1, 4.7])

print(my_array.shape)
print(my_array[2])
print(my_array.ndim) # check dimension

# 2 Dimension array

array_2d =np.array([[1,2,3,9],[5,6,7,8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

# Access the 3rd value in the 2nd row
print(array_2d[1,2])

#Access all the values
print(array_2d[0,:])

# N-array

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])
                           
                           
print(f'We have {mystery_array.ndim} dimensions ')
print(f'The shape is {mystery_array.shape} ')

# Try to access the value 18 in the last line of code.
print(mystery_array[2,1,3])

# Try to retrieve a 1-dimensional vector with the values [97, 0, 27, 18]

print(mystery_array[2,1])

#Try to retrieve a (3,2) matrix with the values 
print(mystery_array[:,:,0])

print('----------------------------------------')

# Challenge 1
# Use .arange()to create a vector a with values ranging from 10 to 29

a = np.arange(0,30)
print(a)


# Challenge 2
# Use Python slicing techniques on a to:
# Create an array containing only the last 3 values of a

# Create a subset with only the 4th, 5th, and 6th values

# Create a subset of a containing all the values except for the first 12 (i.e., [22, 23, 24, 25, 26, 27, 28, 29])

# Create a subset that only contains the even numbers (i.e, every second number)

print(a[-3:])
print(a[3:6])
print(a[12:])
print(a[::2])

# Challenge 3
#Reverse the order of the values in a, so that the first element comes last:

print(np.flip(a))

# Challenge 4
# Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]

b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)
print(nz_indices)

# Challenge 5
# Use NumPy to generate a 3x3x3 array with random numbers

z = random((3,3,3))

print(z)


# Challenge 6
# Use .linspace() to create a vector x of size 9 with values spaced out evenly between 0 to 100 (both included).

x = np.linspace(0, 100, num=9)
print(x)
print(x.shape)

# Challenge 7
# Use .linspace() to create another vector y of size 9 with values between -3 to 3 (both included). Then plot x and y on a line chart using Matplotlib.

y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()

# Challenge 8
#Use NumPy to generate an array called noise with shape 128x128x3 that has random values. Then use Matplotlib's .imshow() to display the array as an image.
#The random values will be interpreted as the RGB colours for each pixel.


noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)
