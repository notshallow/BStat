def binom(n,r):
	if n-r <0:
		return 0
	if n == r or r == 0:
		return 1
	return binom(n-1,r) + binom(n-1,r-1)

n_ = int(input("Please enter the the value of n "))
r_ = int(input("Please enter the the value of r "))

print(binom(n_,r_))