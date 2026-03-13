# Запрашиваем строку с данными
user_input = input("Введите имя, год рождения и средний балл через пробел: ")

# Разделяем строку на части
data_parts = user_input.split()

# Распределяем данные по переменным с преобразованием типов
name = data_parts[0]  # имя остается строкой
birth_year = int(data_parts[1])  # год рождения преобразуем в int
average_score = float(data_parts[2])  # средний балл преобразуем в float

# Вычисляем возраст (текущий год - 2026)
current_year = 2026
age = current_year - birth_year

# Определяем правильное окончание для слова "студент"
student_word = "Студентка" if name.endswith('а') else "Студент"

# Выводим итоговую информацию
print(f"{student_word}: {name}, Возраст: {age} лет, Средний балл: {average_score}")
