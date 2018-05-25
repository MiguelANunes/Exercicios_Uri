def Decifrador(Piscadas):

	Numero_bin = ""

	for Pos in range(len(Piscadas)):
		if(Piscadas[Pos] == '*'):
			Numero_bin = Numero_bin + '1'
		else:
			Numero_bin = Numero_bin + '0'

	Numero_bin = "0b" + Numero_bin

	return Numero_bin


for i in range(3):

	Resultado = 0

	String = input()

	while(String != "caw caw"):

		Numero = Decifrador(String)
		Resultado += int(Numero,2)

		String = input()

	print(Resultado)


