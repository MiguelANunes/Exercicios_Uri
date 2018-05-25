Esqueleto = input()
Classe = input()
Alimentacao = input()

if Esqueleto == "vertebrado":
	if Classe == "ave":
		if Alimentacao == "carnivoro":
			print("aguia")
		elif Alimentacao == "onivoro":
			print("pomba")
	elif Classe == "mamifero":
			if Alimentacao == "onivoro":
				print("homem")
			elif Alimentacao == "herbivoro":
				print("vaca")
elif Esqueleto == "invertebrado":
	if Classe == "inseto":
			if Alimentacao == "hematofago":
					print("pulga")
			elif Alimentacao == "herbivoro":
				print("lagarta")
	elif Classe == "anelideo":
			if Alimentacao == "hematofago":
				print("sanguessuga")
			elif Alimentacao == "onivoro":
				print("minhoca")
