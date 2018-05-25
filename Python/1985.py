Qtd = int(input())
Conta = 0

for i in range(Qtd):
	Number, Amout = map(int,input().split())

	if Number == 1001:
		Conta += Amout * 1.50
	elif Number == 1002:
		Conta += Amout * 2.50
	elif Number == 1003:
		Conta += Amout * 3.50
	elif Number == 1004:
		Conta += Amout * 4.50
	elif Number == 1005:
		Conta += Amout * 5.50

print("{:.2f}".format(Conta))
