def numeric_characteristic(num):
	def is_prime(n):
		if n % 2 == 0:
			return n == 2
		d = 3
		while d * d <= n and n % d != 0:
			d += 2
		return d * d > n
	num = str(num)
	try:
		num = int(num)
		result = True
	except ValueError:
		return f'{num}- не является числом/целым числом'

	if result is True:
		if is_prime(num):
			result = 'Число простое '
		else:
			result = 'Число составное '
		if num % 2 == 0:
			result += 'и чётное.'
		else:
			result += 'и не чётное.'
	return result


print(numeric_characteristic(input("Введите целое число: ")))