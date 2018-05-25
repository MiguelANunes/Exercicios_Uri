def Cryptor(String):

	New_string = ""
	Newer_string = ""

	for Letra in String:
		if(Letra.isalpha()):
			Letra = chr(ord(Letra)+3)
			New_string += Letra
		else:
			New_string += Letra

	New_string = New_string[::-1]

	for i in range(len(New_string)//2, len(New_string)):
		x = chr(ord(New_string[i])-1)
		Newer_string += x

	New_string = New_string[:len(New_string)//2] + Newer_string

	return New_string



Casos = int(input())

for i in range(Casos):
	print(Cryptor(input()))
