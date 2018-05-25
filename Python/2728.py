while True:
	try:
		Cobol = input().split("-")

		if Cobol[0].startswith("c") or Cobol[0].endswith("c") or Cobol[0].startswith("C") or Cobol[0].endswith("C"):
			if Cobol[1].startswith("o") or Cobol[1].endswith("o") or Cobol[1].startswith("O") or Cobol[0].endswith("O"):
				if Cobol[2].startswith("b") or Cobol[2].endswith("b") or Cobol[2].startswith("B") or Cobol[0].endswith("B"):
					if Cobol[3].startswith("o") or Cobol[3].endswith("o") or Cobol[3].startswith("O") or Cobol[0].endswith("O"):
						if Cobol[4].startswith("l") or Cobol[4].endswith("l") or Cobol[4].startswith("L") or Cobol[4].endswith("L"):
							print("GRACE HOPPER")
						else:
							print("BUG")
					else:
						print("BUG")
				else:
					print("BUG")
			else:
				print("BUG")
		else:
			print("BUG")

	except EOFError:
		break
