'''
Created on Nov 18, 2018

@author: Mgmi
'''
import numpy as np
import sys, ast

def arrIntro():    
    #numarr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    list_1=[1,2,3]
    list_2=[4,5,6]
    list_3=[7,8,9]
    numarr1 = np.array([list_1, list_2, list_3])
    # Printing type of arr object 
    print("Array is of type: ", type(numarr1))       
    # Printing array dimensions (axes) 
    print("No. of dimensions: ", numarr1.ndim)      
    # Printing shape of array 
    print("Shape of array: ", numarr1.shape)       
    # Printing size (total number of elements) of array 
    print("Size of array: ", numarr1.size)       
    # Printing type of elements in array 
    print("Array stores elements of type: ", numarr1.dtype)     
    numarr3d = np.array([
                            [
                                [4,6,3,6],
                                [3,7,2,4],
                                [8,3,1,9]
                            ],
                            [
                                [5,6,1,6],
                                [4,7,2,8],
                                [6,3,2,9]
                            ]
                        ])
    # Printing array dimensions (axes) 
    print("No. of dimensions: ", numarr3d.ndim)      
    # Printing shape of array 
    print("Shape of array: ", numarr3d.shape) 
    
    
def arrCreation():
    # Creating array from list with type float 
    a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
    print ("Array created using passed list:\n", a)       
    # Creating array from tuple 
    b = np.array((1 , 3, 2)) 
    print ("\nArray created using passed tuple:\n", b)       
    # Creating a 3X4 array with all zeros 
    c = np.zeros((3, 4)) 
    print ("\nAn array initialized with all zeros:\n", c)       
    # Create a constant value array of complex type 
    d = np.full((3, 3), 6, dtype = 'complex') 
    print ("\nAn array initialized with all 6s." 
                "Array type is complex:\n", d)       
    # Create an array with random values 
    e = np.random.random((2, 2)) 
    print ("\nA random array:\n", e)       
    # Create a sequence of integers  
    # from 0 to 30 with steps of 5 
    f = np.arange(0, 30, 5) 
    print ("\nA sequential array with steps of 5:\n", f)       
    # Create a sequence of 10 values in range 0 to 5 
    g = np.linspace(0, 5, 10) 
    print ("\nA sequential array with 10 values between 0 and 5:\n", g)       
    # Reshaping 3X4 array to 2X2X3 array 
    arr = np.array([[1, 2, 3, 4], 
                    [5, 2, 4, 2], 
                    [1, 2, 0, 1]]) 
      
    newarr = arr.reshape(2, 2, 3) 
      
    print ("\nOriginal array:\n", arr) 
    print ("Reshaped array:\n", newarr) 
      
    # Flatten array 
    arr = np.array([[1, 2, 3], [4, 5, 6]]) 
    flarr = arr.flatten() 
      
    print ("\nOriginal array:\n", arr) 
    print ("Fattened array:\n", flarr)    

def arrCreation2():
    #Given an integer 'x', create an array of size m*n having all integer values equal to 'x'.  
    #Method 1   
    lines = sys.stdin.readlines()
    int_x = int(lines[0])
    rows_m = int(lines[1])
    cols_n = int(lines[2])  
    array_x = np.full((rows_m,cols_n),int_x)    
    print(array_x)
    
    #Method 2
    # Create an array of m*n with all elements equal to 'x' using the tile() function 
    array_x = np.tile(int_x, (rows_m, cols_n))
    print(array_x)
    
    #Method 3
    # Create an array of m*n with all elements equal to '1' using the ones() function
    # and multiply it by 'x'.
    array_x = int_x * np.ones((rows_m, cols_n), dtype = np.int8)
    print(array_x)
    
def arrCreation3(): 

    print ('Enter the dim:')   
    n = int(input())    
    arr=np.array([[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]])
    print(arr)    
    print('Even rows, odd cols', arr[0::2, 1::2])
    print('Odd rows, even cols', arr[1::2, 0::2])    
    #####  Method 1
    x = np.zeros((n, n), dtype = int) 
    print(x)
    #fill with 1 the alternate rows and columns 
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1
    print('After slicing\n',x)
    
    #####  Method 2
    # Create the smallest unit of a checkerboard matrix
    x = np.array([[0, 1], [1, 0]])
    # Create a checkerboard matrix of size n*n using the tile() function. We use n//2 
    # since the smallest unit of a checkerboard matrix is already of size 2*2. So, for 
    # creating a larger matrix, say, of size 8, we need to replicate it using the tile()
    # function 4 times as it will then give a matrix of size 8*8.
    check = np.tile(x, (n//2, n//2))
        # Print the created matrix
    print(check)

def arrCreation4():
    #Extract all the border rows and columns from a 2-D array.
    #Format:
    #Input: A 2-D Python list
    #[[11, 12, 13, 14],
    #[21, 22, 23, 24],
    #[31, 32, 33, 34]]
    #Output: Four NumPy arrays - First column of the input array, first row of the input array, last column of the input array, last row of the input array respectively.
    
    #############   Method 1
    input_str = sys.stdin.read()
    input_list = ast.literal_eval(input_str)
    # Convert the input list to a NumPy array
    array_2d =np.array(input_list)    
    # Extract the first column, first row, last column and last row respectively using
    # appropriate indexing
    col_first = array_2d[:,0]
    row_first = array_2d[0, :]
    col_last = array_2d[:,-1]
    row_last = array_2d[-1,:]    
    print(col_first)
    print(row_first)
    print(col_last)
    print(row_last)
    
    #############   Method 2
    # Extract the number of rows and columns of the array
    rows = len(array_2d[:, 0])
    cols = len(array_2d[0, :])
    
    # Extract the first column, first row, last column and last row respectively using
    # appropriate indexing
    col_1 = array_2d[:, 0]
    row_1 = array_2d[0, :]
    col_last = array_2d[:, cols-1]
    row_last = array_2d[rows-1, :]
    
    print(col_1)
    print(row_1)
    print(col_last)
    print(row_last)

def arrStacking():
    #Array vertical and horizontal stacking    
    #[[[1, 2], [5, 6]], [[3, 4], [7, 8]], [[9, 10, 11, 12]]]
    input_str = sys.stdin.read()
    input_list = ast.literal_eval(input_str)
    list_1 = input_list[0]
    list_2 = input_list[1]
    list_3 = input_list[2]
    
    array_1 = np.array(list_1)
    array_2 = np.array(list_2)
    array_3 = np.array(list_3)
    # Write your code here
    array_hstack=np.hstack((array_1,array_2))
    array_vstack=np.vstack((array_hstack,array_3))
    #print(array_hstack)
    print(array_vstack)



    
if __name__ == '__main__':
    #arrIntro()
    #arrCreation()
    #arrCreation2()
    #arrCreation3()
    #arrCreation4()
    arrStacking()
    