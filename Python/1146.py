X = int(input())

while X != 0:
	for i in range(1,X):
		print("{:d} ".format(i), end="")
	print(X)
	X = int(input())
