while True:
	Problema, Numero = input().split(" ")
	N = ''

	if Problema == '0' and Numero == '0':
		break

	NewNumero = list(filter(lambda ch: ch != Problema, Numero))
	if NewNumero != []:
		N = N.join(x for x in NewNumero)
		print(int(N))
	else:
		print(0)
