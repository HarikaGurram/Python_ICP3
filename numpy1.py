import numpy as np                  #importing Numpy
x = np.random.randint(1,20,15,int)  # creating a random array of size 15 ranging from 1 to 20
x = x.reshape((3,5))                # reshaping above array by 3*5 dimension ----3 rows and 5 colums
print ("An array of 3*5 dimension is :")
print(x)                           # printing out array x
m = (x.max(axis=1).reshape(-1,1))   # considering the max value in a row and taking only one column in the axis and reshaping array into one column
print ("After reshaping :")                           # printing out array x
print(m)
z = (np.where(x==m,x,0))            # creating an array where x==m (max value) and the remaining values will be 0
print ("Max values in a row is :")    
print(z)                       # printing out array z
ans = (x-z)                         # sub z array from x array
print ("replacing the max in each row by 0 :")                         # printing out array after subtraction
print(ans)
