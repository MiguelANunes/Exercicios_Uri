#Não terminado
Casos = int(input())

for i in range(Casos):

	Soldados, Step = map(int,input().split())
	Death_row = [1 for x in range(Soldados)]
	Index = 0

	while Death_row.count(1) != 1:

		for Index in range(len(Death_row)):
			
			if Death_row.count(1) == 1:
				break

			elif Death_row[Index] == 1:
				print(Death_row)
				print(Index)
				if Index + (Step-1) < len(Death_row) and Death_row[Index + (Step-1)] == 1:
					Death_row[Index + (Step-1)] -= 1
				elif Death_row[(Index + (Step-1))-len(Death_row)] == 1:
					Death_row[(Index + (Step-1))-len(Death_row)] -= 1

			else:
				continue

	print(Death_row)

	for j in range(len(Death_row)):
		if Death_row[j] == 1:
			break

	print("Case {:d}: {:d}".format((i+1), j+1))
