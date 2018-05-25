Casos = int(input())

for i in range(Casos):

	Maior, Menor = input().split(" ")

	if len(Maior) > len(Menor):
		if Maior.endswith(Menor):
			print("encaixa")
		else:
			print("nao encaixa")

	elif len(Maior) == len(Menor):
		if Maior == Menor:
			print("encaixa")
		else:
			print("nao encaixa")

	elif len(Maior) < len(Menor):
		print("nao encaixa")
