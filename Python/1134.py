Codigo = int(input())
Alcool = 0
Gasolina = 0
Diesel = 0

while Codigo != 4:
	if Codigo == 1:
		Alcool += 1
	elif Codigo == 2:
		Gasolina += 1
	elif Codigo == 3:
		Diesel += 1
	Codigo = int(input())
print("MUITO OBRIGADO")
print("Alcool: {:d}\nGasolina: {:d}\nDiesel: {:d}".format(Alcool, Gasolina, Diesel))
