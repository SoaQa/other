def string_parser(input_string):
	def up_char(word):
		l_word = list(word)
		l_word[0] = l_word[0].upper()
		return ''.join(l_word)
	my_list = input_string.split('\x20')
	return  f'Количество слов в строке - {len(my_list)}.\n' \
			f'Строка отсортированная по возрастанию - {" ".join(sorted(my_list)).replace(".", "")}.\n' \
			f'Делаем первые буквы заглавными - {" ".join([up_char(w) for w in my_list]).replace(".", "")}.'


print(string_parser(input("Введите строку, разделитель пробел: ")))
