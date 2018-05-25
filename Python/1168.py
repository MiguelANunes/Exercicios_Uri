Casos = int(input())
Leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

for i in range(Casos):

	Numero = input()
	Total = 0

	for Digito in Numero:
		Total += Leds[Digito]

	print("{:d} leds".format(Total))
