
while True:
	try:
		Int1, Int2 = map(int, input().split())

		print("{:d}".format(Int1^Int2))
	except EOFERROR:
		break
