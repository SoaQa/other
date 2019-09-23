def find_palindromes(x):
	result = list()
	for j in x:
		if j == int(str(j)[::-1]):
			result.append(j)
	return result


print("Вводите числа по одному и/или списком через запятую.\nДля завершения ввода нажмите enter")

seq = list()

while True:
	input_data = input()
	if len(input_data) == 0:
		break
	try:
		if len(input_data.split(',')) > 1:
			for i in input_data.split(','):
				seq.append(int(i.strip()))
		else:
			seq.append(int(input_data))
	except ValueError:
		print("Вводите только целые числа")

print('Найденные палиндромы: ', find_palindromes(seq))

