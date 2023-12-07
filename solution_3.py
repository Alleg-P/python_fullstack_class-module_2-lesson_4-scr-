# Задача 3: Конвертация валют

price = float(input("Введите цену товара ($): "))

dollar = float(input("Введите курс доллара (руб.): "))

rubles = price * dollar

print("Цена товара (руб.): ", round(rubles, 1))
