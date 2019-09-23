def get_nodnok(x, y):
	x = str(x)
	y = str(y)
	try:
		x = int(x)
		y = int(y)
		result = True
	except ValueError:
		return 'Одно из чисел введено не корректно'
	if result is True:
		m = x * y
		while x != 0 and y != 0:
			if x > y:
				x %= y
			else:
				y %= x
		result = f'НОД = {x + y}, НОК = {m // (x + y)}'
		return result


print(get_nodnok(x=input("Введите первое число: "), y=input("Введите второе число: ")))