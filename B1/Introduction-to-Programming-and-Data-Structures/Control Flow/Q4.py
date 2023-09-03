'''
Implement the Chatterjee Correlation Coefficient (Chatterjee,
JASA 2001) in python. Note that, your inputs are two sets of
real values and the output is also a real value.
Link to the paper: https://www.tandfonline.com/doi/
full/10.1080/01621459.2020.1758115
'''
import random
from functools import cmp_to_key

xl = input("Enter the set of X_i's seperated by space \n")
yl = input("Enter the set of Y_i's seperated by space \n")

xl = xl.split()
yl = yl.split()

ls = []

for i in range(0, len(xl)):
	ls.append((int(xl[i]),int(yl[i])))

# print(ls)

def compare_with_ties(x,y):
    if x[0] <= y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        return random.choice([-1, 1])

random.shuffle(ls)
ls = sorted(ls, key = cmp_to_key(compare_with_ties))

rank_list = []
l_list = []
len = len(ls)
for i in range(0,len):
	rank = 0
	l = 0
	for j in range(0,len):
		if ls[j][1] >= ls[i][1]:
			l += 1
		if ls[j][1] <= ls[i][1]:
			rank += 1
	rank_list.append(rank)
	l_list.append(l)

sigma1 = 0

for i in range(0,len-1):
	sigma1 = sigma1+abs(rank_list[i+1]-rank_list[i])

sigma2 = 0

for i in range(0,len-1):
	sigma2 = sigma2 + l_list[i]*(len - l_list[i])

final_Value = 1- len*sigma1/(2*sigma2)

print(final_Value)