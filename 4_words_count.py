import re


def words_count(pattern, string):
	result = re.findall(pattern, string, flags=re.IGNORECASE)
	return f'Количество совпадений {len(result)}.'


print(words_count(input("Введите паттерн для поиска: "), input("Введите строку для поиска: ")))
