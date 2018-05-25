def to_roman(Number):
	Roman_Numbers = {1 : 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',900: 'CM',1000: 'M'}
	Temp_num = [x for x in str(Number)]
	Result = ''
	Numbers = dict.keys(Roman_Numbers)
	print()

	if Number > 99:
		Temp_num[0] += '00'
		Temp_num[1] += '0'
	elif Number <= 99:
		Temp_num[0] += '0'

	Temp_num = [int(i) for i in Temp_num]

	for N in Temp_num:

		if N in Numbers:
			Result += Roman_Numbers[N]
		else:
			for X in range(len(Numbers)):
				if Numbers[X] < N and N < Numbers[X+1]:
					print(N-Roman_Numbers[Numbers[X]])


to_roman(int(input()))
