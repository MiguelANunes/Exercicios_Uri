def Fib(N):
	A,B = 0,1
	for i in range(N-1):
		print("{:d}".format(A), end = " ")
		A,B = B, A+B
	return A

X = int(input())
print(Fib(X))
