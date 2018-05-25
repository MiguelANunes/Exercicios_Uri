Tautograma = input()
while Tautograma != '*':

	Palavras = Tautograma.split(" ")
	Inicio = []

	for Palavra in Palavras:
		Inicio.append(Palavra[0].lower())

	if Inicio[1:] == Inicio[:-1]:
		print("Y")
	else:
		print("N")

	Tautograma = input()
