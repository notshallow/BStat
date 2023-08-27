'''
A number is PSEUDOPERFECT if the sum of all or some of 
its proper divisors is equal to the number itself. Write a
program to verify whether a given number is pseudoperfect or 
not. E.g., 12 is a pseudoperfect number from its divisors 1, 2, 
3, 4 and 6, we can ignore 4 and derive 1 + 2 + 3 + 6 = 12.
'''

from math import sqrt

mynum = int(input("Please input a number to verify:\n"))

factors = []

factors.append(1)

for i in range(2,int(sqrt(mynum))+1):
	if mynum % i == 0:
		factors.append(i)
		factors.append(int(mynum/i))

factors = sorted(list(set(factors)))

mybool = False

for i in range(1<<len(factors)):
	vec = []
	for j in range(len(factors)):
		if (i & (1 << j))!=0:
			vec.append(factors[j])
	if sum(vec)==mynum:
		mybool = True

if mybool:
	print(f"Yes, {mynum} is a pseudoperfect number")
else:
	print(f"No, {mynum} is NOT a pseudoperfect number")