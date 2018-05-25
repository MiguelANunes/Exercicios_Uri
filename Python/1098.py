I = 0
J = 1
x = 0

while(I <= 2):

	for i in range(3):
		if (I == int(I)) or (J == int(J)):
			print("I={:.0f} J={:.0f}".format(I,J))
		else:
			print("I={:.1f} J={:.1f}".format(I,J))
		J += 1
	x += 1
	J -= 3
	I += 0.2
	J += 0.2
	if(x == 5 or x == 10 or x == 15):
		I = round(I)
		J = round(J)
