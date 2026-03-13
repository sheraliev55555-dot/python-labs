# Запрашиваем номер карты (16 цифр)
card_number = input("Введите номер карты (16 цифр): ")

# Извлекаем последние 4 цифры
last_four = card_number[12:16]  # или card_number[-4:]

# Формируем замаскированный номер
masked_number = f"**** **** **** {last_four}"

# Выводим результат
print(masked_number)
