Casos = int(input())

for i in range(Casos):
# Ordem = 1º dec, 2º hex, 3º bin
	Number, Base = input().split()

	if Base == "bin":
		print("Case {:d}:".format(i+1))
		print("{:d} dec".format(int(Number,2)))
		print("{:x} hex".format(int(Number,2)))
	elif Base == "dec":
		print("Case {:d}:".format(i+1))
		print("{:x} hex".format(int(Number)))
		print("{:b} bin".format(int(Number)))
	elif Base == "hex":
		print("Case {:d}:".format(i+1))
		print("{:d} dec".format(int(Number,16)))
		print("{:b} bin".format(int(Number,16)))

	print("")
