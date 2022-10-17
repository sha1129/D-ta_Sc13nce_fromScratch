# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:36:50 2020

"""

import numpy as np

my_list = [1,2,3]

#casting
ar= np.array(my_list)

my_mat = [[1,2,3],[4,5,6],[66,6,6]]

n_mat = np.array(my_mat)

#array of 1 to 20 by 3
np.arange(1,20,3)

#zeros and ones and eye array
np.zeros(3)
#lines and columns 
np.zeros((2,2))

#ones 
np.ones(3)
#ones column 
np.ones((1,1))

#eye identity matrix daigonal of 1s must be squared
np.eye(3)

#line space even space number
np.linspace(1,10,10)

#random
np.random.rand(3)
 
#columns 
np.random.rand(4,4)

###random normal distrobution 
np.random.randn(3)

#normal distribution column
np.random.randn(4,4)

####random int one number between 10
np.random.randint(10)

#random int one to 10 but one number
np.random.randint(1,10,10)

arr = np.arange(25)
ran_arr = np.random.randint(1,100,25)

#reshape method but have to be the same dimension must be same size
# need to know how many values
arr.reshape(5,5)

#min max find
ran_arr.max()
ran_arr.min()

#location index find of max
ran_arr.argmax()

#reshape to matrix value from vecti
arr_mat2 = arr.reshape(5,5)

#check the shape of an array vector or matrix
arr_mat2.shape

#finally knowing the datatype 
arr.dtyp








