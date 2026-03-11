# Задание 2. Конвертер валют (Рубли в Доллары)
# Использование модуля decimal для точных финансовых вычислений

from decimal import Decimal, ROUND_HALF_UP

# 1. Запрашиваем данные у пользователя
# Мы используем Decimal вместо float для точности
rubles_input = input("Введите сумму в рублях: ")
rate_input = input("Введите текущий курс доллара: ")

# Преобразуем введенные строки в объекты Decimal
rubles = Decimal(rubles_input)
rate = Decimal(rate_input)

# 2. Вычисляем сумму в долларах
dollars = rubles / rate

# 3. Округляем результат до 2 знаков после запятой (центы)
# Метод quantize помогает сделать округление правильным
final_dollars = dollars.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# 4. Выводим результат
print(f"Сумма в рублях: {rubles} руб.")
print(f"Курс доллара: {rate}")
print(f"Итого в долларах: {final_dollars} USD")
