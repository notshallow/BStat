'''
print the following when input = 5
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
'''
p = int(input("Please enter the number of lines you want the pattern to be (must be odd): "))

if p % 2 == 0:
    print("You entered an even number!!!")
else:
    n = int((p+1)/2)

    for i in range(1, n):
        for j in range(1, n):
            l =  min(i,j)
            print(n - l + 1, end = " ")

        for j in range(n, 0, -1):
            l =  min(i,j)
            print(n - l + 1, end = " ");
        print();

    for i in range(n, 0, -1):
        for j in range(1, n + 1):
            l =  min(i,j)
            print(n - l + 1, end = " ")
        for j in range(n-1, 0, -1):
            l =  min(i,j)
            print(n - l + 1, end = " ")
     
        print()