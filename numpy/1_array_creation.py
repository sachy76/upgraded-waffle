import numpy as np


#Print the numpy version and the configuration
#print(np.__version__)
#np.show_config()


# Create a null vector of size 10
Z = np.zeros(10)
#print(Z)


# How to find the memory size of any array
Z = np.zeros((10,10))
#print("%d bytes" % (Z.size * Z.itemsize))

# Create a null vector of size 10 but the fifth value which is 1
Z = np.zeros(10)
Z[4] = 1
Z

# Create a vector with values ranging from 10 to 49
Z = np.arange(10,50)
Z


# Reverse a vector (first element becomes last)
Z = np.arange(50)
Z = Z[::-1]
Z

# Create a 3x3 matrix with values ranging from 0 to 8 
Z = np.arange(9).reshape(3,3)
Z


# Find indices of non-zero elements from [1,2,0,0,4,0] 
nz = np.nonzero([1,2,0,0,4,0])
nz

# Create a 3x3 identity matrix
Z = np.eye(3)
Z


# Create a 3x3x3 array with random values
Z = np.random.random((3,3,3))
Z

# Create a 10x10 array with random values and find the minimum and maximum values
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
Zmin, Zmax


# Create a random vector of size 30 and find the mean value
Z = np.random.random(30)
m = Z.mean()
m


# Create a 2d array with 1 on the border and 0 inside
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
Z


# How to add a border (filled with 0's) around an existing array
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
Z

# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
Z = np.diag(1+np.arange(4),k=-1)
Z

# Create a 8x8 matrix and fill it with a checkerboard pattern
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
Z

# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
np.unravel_index(100,(6,7,8))


# Create a checkerboard 8x8 matrix using the tile function 
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
Z


# Normalize a 5x5 random matrix
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
Z

# Create a custom dtype that describes a color as four unsigned bytes (RGBA)
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])



















