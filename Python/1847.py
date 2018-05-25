def Felicidade(Temp1, Temp2, Temp3):
	
	if(Temp1 > Temp2 and Temp3 >= Temp2): #certo
		return True

	if(Temp2 > Temp1 and Temp3 > Temp2 and (Temp3 - Temp2) >= (Temp2 - Temp1)): #
		return True

	if(Temp1 > Temp2 and Temp2 > Temp3 and (Temp1 - Temp2) > (Temp2 - Temp3)): #
		return True

	if(Temp1 == Temp2 and Temp3 > Temp2): #
		return True

	if(Temp2 > Temp1 and Temp2 >= Temp3): # certo
		return False

	if(Temp2 > Temp1 and Temp3 > Temp2 and (Temp2 - Temp1) > (Temp3 - Temp2)): #
		return False

	if(Temp2 > Temp1 and Temp3 > Temp2 and (Temp3 - Temp2) >= (Temp2 - Temp1)): #
		return False

	if(Temp1 == Temp2 and Temp2 > Temp3): #
		return False


T1, T2, T3 = map(int, input().split())

if(Felicidade(T1,T2,T3)):
	print(":)")

else:
	print(":(")