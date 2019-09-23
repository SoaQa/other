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


some_goods = {"фотоаппарат": {"weight": 1, "cost": 10000}, "Мешок угля": {"weight": 20, "cost": 1000}, \
				"Ноутбук": {"weight": 3, "cost": 20000}, "Телефон": {"weight": 0.3, "cost": 15000}, \
				"Тостер": {"weight": 5, "cost": 2000}, "Кроссовки": {"weight": 2, "cost": 3000}}

new_backpack1 = BackPack(goods=some_goods, max_weight=22)

new_backpack2 = BackPack(goods=some_goods, max_weight=10)

new_backpack3 = BackPack(goods=some_goods, max_weight=5)

print(new_backpack1)

print(new_backpack2)

print(new_backpack3)