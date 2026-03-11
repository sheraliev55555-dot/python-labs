# Задание 3. Банковский вклад (Расчет процентов по карте)
# Используем decimal для точности финансовых расчетов

from decimal import Decimal, ROUND_HALF_UP

# 1. Запрашиваем данные у пользователя
# Мы запрашиваем сумму и процент как текст и переводим в Decimal
amount_input = input("Введите текущую сумму на карте: ")
percent_input = input("Введите годовой процент (например, 10): ")

amount = Decimal(amount_input)
percent = Decimal(percent_input)

# 2. Вычисляем маблағи фоиз (Сумма * Процент / 100)
interest = (amount * percent) / Decimal("100")

# 3. Итоговая сумма = исходная сумма + проценты
total = amount + interest

# 4. Округляем до 2 знаков после запятой (тинҳо/копейки)
final_total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# 5. Вывод результата
print(f"Исходная сумма: {amount} руб.")
print(f"Процентная ставка: {percent}%")
print(f"Итоговая сумма через год: {final_total} руб.")
