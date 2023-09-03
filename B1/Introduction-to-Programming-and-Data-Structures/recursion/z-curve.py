import numpy as np

def z_func(x1,y1,x2,y2,arr):

	if (x1 == x2) and (y1 == y2):
		print(arr[x1][y1], end = " ")
	else:
		z_func(x1,y1,(x1+x2)//2,(y1+y2)//2,arr) 
		z_func(x1,(y1+y2)//2 + 1,(x1+x2)//2,y2,arr)
		z_func((x1+x2)//2 +1, y1,x2,(y1+y2)//2,arr)
		z_func((x1+x2)//2 +1, (y1+y2)//2 +1, x2,y2,arr)

m = int(input("Please enter m to create 2^m * 2^m matrix"))

my_arr = np.reshape(np.arange(1,2**(2*m)+1),(2**m,2**m))

z_func(0,0,3,3,my_arr)