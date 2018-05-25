Casos = int(input())

for i in range(Casos):
	Comida = float(input())
	Dias = 0

	while Comida > 1:
		Comida /= 2
		Dias += 1

	print("{:d} dias".format(Dias))
