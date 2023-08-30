'''
123456789
456789123
789123456
234567891
567891234
891234567
345678912 
678912345 
912345678
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