f_par = lambda X: X%2 == 0

Par = [None] * 5
Impar = [None] * 5

p = 0
im = 0
for i in range(15):
	T = int(input())

	if f_par(T):
		Par[p] = T
		p += 1
	else:
		Impar[im] = T
		im += 1

	if im == 5:
		for j in range(5):
			print("impar[{:d}] = {:d}".format(j,Impar[j]))
			Impar[j] = None
		im = 0
	if p == 5:
		for h in range(5):
			print("par[{:d}] = {:d}".format(h,Par[h]))
			Par[h] = None
		p = 0

for i in range(im):
	print("impar[{:d}] = {:d}".format(i,Impar[i]))

for j in range(p):
	print("par[{:d}] = {:d}".format(j,Par[j]))
