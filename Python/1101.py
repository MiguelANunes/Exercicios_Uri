while(True):
	S = 0

	(M,N) = map(int, input().split())
	if(M <= 0 or N <= 0):
		break

	if M >= N:
		for i in range(N,M+1):
			print("{:d}".format(i), end=' ')
			S += i
		print("Sum={:d}".format(S))

	elif N > M:
		for i in range(M,N+1):
			print("{:d}".format(i), end=' ')
			S += i
		print("Sum={:d}".format(S))
