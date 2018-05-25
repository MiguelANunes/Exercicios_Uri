Vetor = [0 for i in range(20)]
for i in range(20):
	Vetor[i] = int(input())

J = 19
for i in range(9):
	Vetor[i], Vetor[J] = Vetor[J], Vetor[i]
	J -= 1

for h in range(20):
	print("N[{:d}] = {:d}".format(h,Vetor[h]))
