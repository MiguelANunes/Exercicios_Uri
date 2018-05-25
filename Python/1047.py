Horario = [int(i) for i in input().split()]
Delta = ((Horario[0]*60)+(Horario[1])-((Horario[2]*60)+(Horario[3])))
Delta *= (-1 if Delta < 0 else 1)
Horas = 0

while(Delta > 60):
	Horas += 1
	Delta -= 60
print(Delta)
print(Horas)
if (Delta == 0 and Horas == 0):
	print("O JOGO DUROU 24 HORA(S) E 0 MINUTOS(S)")
else:
	print("O JOGO DUROU {:d} HORA(S) E {:d} MINUTOS(S)".format(Horas,Delta))
