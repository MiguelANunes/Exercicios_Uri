def moves(X,Y):
		M = []

		T1, T2, i, j = 1, 1, 1, 1
		while T1 <= 8 and T2 <= 8:
			T1 = X + i
			T2 = Y + j
			i += 1
			j += 1
			M.append((T1,T2))

		T1, T2, i, j = 1, 1, 1, -1
		while T1 <= 8 and T2 >= 1:
			T1 = X + i
			T2 = Y + j
			i += 1
			j -= 1
			M.append((T1,T2))

		T1, T2, i, j = 1, 1, -1, 1
		while T1 >= 1 and T2 <= 8:
			T1 = X + i
			T2 = Y + j
			i -= 1
			j += 1
			M.append((T1,T2))

		T1, T2, i, j = 1, 1, -1, -1
		while T1 >= 1 and T2 >= 1:
			T1 = X + i
			T2 = Y + j
			i -= 1
			j -= 1
			M.append((T1,T2))

		M = list(set(M)) # Removendo tuplas repetidas (e destruindo a ordenação)

		return M


(X1, Y1, X2, Y2) = map(int, input().split())
while(True):
	try:

		Movs = moves(X1,Y1)

		if (X2,Y2) == (X1,Y1):
			print("0")

		elif (X2,Y2) in Movs or X2 == X1 or Y1 == Y2:
			print("1")

		else:
			print("2")


		(X1, Y1, X2, Y2) = map(int, input().split())
		if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
			break

	except EOFError:
		break
