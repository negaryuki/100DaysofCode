import numpy as np

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
