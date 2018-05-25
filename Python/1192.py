Casos = int(input())

for i in range(Casos):

	Jogo = input()

	if int(Jogo[0]) != int(Jogo[2]):
		if Jogo[1].islower():
			print(int(Jogo[0])+int(Jogo[2]))
			continue
		else:
			print(int(Jogo[2])-int(Jogo[0]))
	else:
		print(int(Jogo[0])*int(Jogo[2]))
