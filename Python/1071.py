S = 0

X = int(input().split())
Y = int(input().split())

if X > Y:
	for i in range(Y+1,X):
		if i % 2 != 0:
			S += i
	print(S)

elif Y > X:
	for i in range(X+1,Y):
		if i % 2 != 0:
			S += i
	print(S)

elif Y == X:
	print(0)
