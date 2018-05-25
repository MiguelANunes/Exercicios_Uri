even = (lambda x: x % 2 == 0)

while True:

	try:
		Sentenca = input()
		NewSetenca = ''
		i = 0

		for Letra in Sentenca:
			if not Letra.isspace():
				NewSetenca += Letra.upper() if even(i) else Letra.lower()
				i += 1
			else:
				NewSetenca += ' '

		print(NewSetenca)

	except EOFError:
		break
