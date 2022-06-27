# Логические операции. Оператор in
# Условные операторы

# 1. Логические операции and, or, not. Оператор in, not in
# 2. Создание простого условия
# 3. Вложенные условия
# 4. Проверка булевых переменных
# 5. Операторы else, elif. Вложенные конструкции if
# 6. Тернарный оператор




# ---- 1. Логические операции. Оператор in ----

# 1. and (логическое умножение). Возвращает True, если оба выражения равны True
age = 22
weight = 58
result = age > 21 and weight == 58
print(result)  # True

# 2. or (логическое сложение). Возвращает True, если хотя бы одно из выражений равно True
age = 22
isMarried = False
result = age > 21 or isMarried
print(result)  # True, так как выражение age > 21 равно True

# 3. not (логическое отрицание). Возвращает True, если выражение равно False
age = 22
isMarried = False
print(not age > 21)  # False
print(not isMarried)  # True

# 4. Оператор in возвращает True если в некотором наборе значений есть определенное значение. Он имеет следующую форму: значение in набор_значений
message = "hello world!"
hello = "hello"
print(hello in message)  # True - подстрока hello есть в строке "hello world!"
 
gold = "gold"
print(gold in message)  # False - подстроки "gold" нет в строке "hello world!"

# 5. not in. Возвращает True, если в наборе значений НЕТ определенного значения:
message = "hello world!"
hello = "hello"
print(hello not in message)  # False
 
gold = "gold"
print(gold not in message)  # True




# ---- 2. Создание простого условия ----

if 5 == 5:
    print('Yes', end='')
    print('!!!')





# ---- 3. Вложенные условия ----
user_data = int(input('Введите число: '))

if user_data != 5:
    print('Первое условие выполнено')
    if user_data > 6:
        print('Второе условие выполнено')




# ---- 4. Проверка булевых переменных ----
isHappy = True
if isHappy:
    print('User is happy')

isHappy = False
if not isHappy:
    print('User is not happy')




# ---- 5. Операторы else, elif. Вложенные конструкции if ----
language = "ukrainian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")




# ---- 6. Тернарный оператор ----

# Стандартная запись
data = input()

if data == 'Five':
    number = 5
else:
    number = 0

print(number)

# Тернарный оператор - по сути оператор if else, просто записывается в одну строку
data = input()
number = 5 if data == 'Five' else 0
print(number)