import time as ti
def fibo(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

k = int(input("Please enter n: "))

s = ti.time()
print(f"First {k} numbers in fibonacci series are: ",*fibo(k-1))
e = ti.time()

print(f"Time taken to calculate the fibonacci series is {1000*(e-s)}ms")