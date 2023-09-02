'''
Given a list of non-negative digits (0-9), not necessarily
distinct, write a program to find out the largest multiple of 3
that can be formed from these digits. E.g., if the sample input
19234493219, the output will be 9994433211.
'''

n = int(input("please input list of digits\n"))

temp = n
modsum = 0
arr = [0,0,0,0,0,0,0,0,0,0]

while temp:
	modsum += (temp%10)
	arr[temp%10]+=1
	temp//=10

modsum %=3

one_mod = [1,4,7]
two_mod = [2,5,8]

def arr_maker(some_arr,first,second):
	flag = True
	for i in first:
		if some_arr[i] != 0:
			some_arr[i]-=1
			flag = False
			break

	if flag:
		count = 2
		while count:
			for i in second:
				if some_arr[i] != 0:
					some_arr[i]-=1
					count-=1
					break

if modsum == 1:
	arr_maker(arr,one_mod,two_mod)
if modsum == 2:
	arr_maker(arr,two_mod,one_mod)

s = str()

for i in range(9,-1,-1):
	s+=str(i)*arr[i]
		
print("the largest multiple of 3 that can be formed from these digits is : ",s)