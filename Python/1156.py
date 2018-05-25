S = 0
Div = 1

for i in range(1,40):
	if i % 2 != 0:
		S += i/Div
		Div *= 2
print("{:.2f}".format(round(S)))
