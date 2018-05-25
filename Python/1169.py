Casos = int(input())

for i in range(Casos):

	Casas = int(input())
	Graos = 1

	for j in range(Casas):
		Graos *= 2
	
	Graos /= 12000

	if Graos < 1:
		print("0 kg")
	else:
		print("{:d} kg".format(int(Graos)))
