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
	return result, result_cost, result_weight


some_goods = {"фотоаппарат": {"weight": 1, "cost": 100}, "Мешок угля": {"weight": 20, "cost": 10}, \
				"Ноутбук": {"weight": 3, "cost": 200}, "Телефон": {"weight": 0.3, "cost": 150}, \
				"Тостер": {"weight": 5, "cost": 20}, "Кроссовки": {"weight": 2, "cost": 30}}


print(backpack(some_goods, 10))



