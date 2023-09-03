'''
Consider an n-digit number. Square it and add the right n
digits to the left n or n − 1 digits. If the resultant sum is same
as the original number, then it is called a Kaprekar number.
E.g., 45 is a Kaprekar number. Write a program to verify
whether a given number is Kaprekar or not.
'''
n=int(input("please enter a number: "))
sq=n*n
count=0
temp = n

while temp:
	count+=1
	temp//=10

right=sq%(10**count)
sq//=10**count
if sq+right==n:
	print(n, "is a Kaprekar number")
else:
	print(n, "is not a Kaprekar number")