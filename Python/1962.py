Casos = int(input())

for i in range(Casos):

	Anos = int(input())
	Anos = 2015 - Anos

	if Anos == 0:
		print("1 A.C.")
		continue
	elif Anos > 0:
		print("{:d} D.C.".format(Anos))
		continue
	elif Anos < 0:
		Anos *= -1
		Anos += 1
		print("{:d} A.C.".format(Anos))
