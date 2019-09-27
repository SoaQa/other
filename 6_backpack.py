some_goods = {"фотоаппарат": {"weight": 1, "cost": 100}, "Мешок угля": {"weight": 20, "cost": 10}, \
				"Ноутбук": {"weight": 3, "cost": 200}, "Телефон": {"weight": 0.3, "cost": 150}, \
				"Тостер": {"weight": 5, "cost": 20}, "Кроссовки": {"weight": 2, "cost": 30}}


#Метод динамического программирования

def backpack(goods, max_weight):
	t = {0:0}
	sol = {0:[]}
	for i in goods:
		t_old = dict(t)
		for x in t_old:
			if x + goods[i]["weight"] <= max_weight:
				if (x + goods[i]["weight"] in t) or ((x + goods[i]["weight"]) < (t_old[x] + goods[i]["cost"])):
					t[x + goods[i]["weight"]] = (t_old[x] + goods[i]["cost"])
					sol[x + goods[i]["weight"]] = sol[x] + [i]
	result_cost = max(t.values())
	result_weight = None
	for i in t:
		if t[i] == result_cost:
			result_weight = i
	#print(sol)
	#print(t)
	result = sol[result_weight]
	return {"Вещи в рюкзаке": result}, {"Стоимость":result_cost}, {"Вес":result_weight}


print("Ваирант 1\n", backpack(some_goods, 10))


#Жадный алгоритм


class BackPack(object):

	def __init__(self, goods, max_weight):
		self.goods = goods
		self.max_weight = max_weight
		self.total_weight = 0
		self.items_inside = self.fill_backpack()

	def fill_backpack(self):
		#Сортируем вещи по удельной стоимости
		sorted_goods = sorted(self.goods.items(), key=lambda x: x[1]["weight"] / x[1]["cost"])
		result = dict()
		#Заполняем рюкзак, если вещь не помещается пробуем следующую, по мере уменьшения удельной стоимости
		for i in sorted_goods:
			if self.total_weight + i[1]["weight"] < self.max_weight:
				result.update({i[0]: i[1]})
				self.total_weight += i[1]["weight"]
		return result

	def __str__(self):
		return f'Вещи в рюкзаке: {self.items_inside}.\nСуммарный вес: {self.total_weight}'


new_backpack1 = BackPack(goods=some_goods, max_weight=10)


print("\nВаирант 2\n", new_backpack1)






