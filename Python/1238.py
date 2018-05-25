Casos = int(input())

for i in range(Casos):

	Primeira, Segunda = input().split()
	j = 0
	NewString = ''

	for LP,LS in zip(Primeira, Segunda):
		NewString += LP
		NewString += LS
		j += 1

	if len(Primeira) > len(Segunda):
		NewString += Primeira[j:]

	elif len(Primeira) < len(Segunda):
		NewString += Segunda[j:]

	print(NewString)
