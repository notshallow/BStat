'''
An n-digit number is SPECIAL if the addition of its sum of the 
digits and the product of its digits equals to the original 
number. E.g., 19 is a SPECIAL 2-digit number. Write a
program to verify whether a given number is SPECIAL or not.
Extend this program to verify whether there exists any
SPECIAL number for a given value of number of digits n.
'''
def sumof(n):
	s=0
	p=1
	temp=n
	while n:
		s+=(n%10)
		n//=10
	n=temp
	while n:
		p*=(n%10)
		n//=10
	return p+s
k=int(input("please enter your number of digits \n"))
coun=0
for i in range(10**(k-1),10**k):
	if i==sumof(i):
		coun+=1
		print(i)
print(coun)