while True:

	Casos = int(input())
	if Casos == 0:
		break

	DivX, DivY = map(int, input().split())
	for i in range(Casos):

		CasaX, CasaY = map(int, input().split())

		if CasaX == DivX or CasaY == DivY:
			print("divisa")
			continue
		elif CasaX > DivX and CasaY > DivY:
			print("NE")
			continue
		elif CasaX > DivX and CasaY < DivY:
			print("SE")
			continue
		elif CasaX < DivX and CasaY > DivY:
			print("NO")
			continue
		elif CasaX < DivX and CasaY < DivY:
			print("SO")
			continue
