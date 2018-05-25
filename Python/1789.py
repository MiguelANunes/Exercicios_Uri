while True:
	try:

		Total = int(input())

		L = input().split(" ")
		Lesmas = [int(x) for x in L]

		Rapida = max(Lesmas)

		if Rapida <= 10:
			print("1")
			continue
		elif Rapida > 10 and Rapida < 20:
			print("2")
			continue
		elif Rapida >= 20:
			print("3")
			continue

	except EOFError:
		break
