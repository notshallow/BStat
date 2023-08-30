'''Write a program that takes a 9 × 9 matrix as input and 
checks whether it is a valid Sudoku matrix or not. Recall that 
a Sudoku matrix is filled in with numbers from 1-9 with no 
repeated numbers in each line, horizontally or vertically. E.g., 
the following is a valid Sudoku matrix.
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3 
7 8 9 1 2 3 4 5 6 
2 3 4 5 6 7 8 9 1 
5 6 7 8 9 1 2 3 4
8 9 1 2 3 4 5 6 7 
3 4 5 6 7 8 9 1 2 
6 7 8 9 1 2 3 4 5 
9 1 2 3 4 5 6 7 8
'''

sudoku = []
for i in range(9):
	sudoku.append([int(j) for j in input(f"Enter row number {i+1}: ").split()])

def check_sub_matrix(arr,x,y):
	s = 0
	for i in range(x,x+3):
		for j in range(y,y+3):
			s += arr[i][j]
	return s

flag = True

for i in range(9):
	sumi = 0
	sumj = 0
	for j in range(9):
		sumj += sudoku[i][j]
		sumi += sudoku[j][i]
	if (sumi != 45) or (sumj != 45):
		flag = False
		break;

num = [0,3,6]

for i in num:
	for j in num:
		if check_sub_matrix(sudoku,i,j) != 45:
			flag = False

if flag:
	print("Given matrix is a VALID sudoku solution")
else:
	print("Given matrix is a INVALID sudoku solution")