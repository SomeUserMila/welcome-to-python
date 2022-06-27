# Переменные и типы данных

# 1. Переменные
# 2. Типы данных
# 3. Приведение к типам данных
# 4. Работа с пользователем (корректная работа с типами данных)



# ---- 1. Переменные ----

number = 5
print("Result:", number) # Result: 5
number = 7
print("Result:", number) # Result: 7

del number # удаление переменной
# Если написать print("Result:", number) то выведет ошибку: Exception has occurred: NameError name 'number' is not defined

digit = 4.6588 # можно выводить в т.ч. дробные числа, положительные, отрицательные
word = "Result" 
word_ets = 'Result' 
boolean = True 
boolean = False 
found = None # может создать переменную, но изначально не присваивать ей никакое значение (None)



# ---- 2. Типы данных ----

'''
int - целое число
float - десятичное число
string - строка
bool - булевая переменная
'''



# ---- 3. Приведение к типам данных ----

# str() - приведение к строке, 
num = 5
word = 'Result: '
print(word + str(num)) # Result: 5

# int() - приводит к числу
num = 5
str_num = '5'
print(num + int(str_num)) # 10

# двойное приведение
num = 5
word = 'Result: '
str_num = '5'
print(word, num + int(str_num), sep='') # Result: 10 - 1й способ
print(word + str(num + int(str_num))) # Result: 10 - 2й способ

# float() - преобразование к типу данных float

# bool() - преобразование к булевому типу данных



# ---- 4. Работа с пользователем ----
num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
print(num1)
print(num2)
print('Result:', num1 + num2) # num1 = 4 num2 = 1 - Result: 41
# print('Result:', num1 / num2) # Exception has occurred: TypeError unsupported operand type(s) for /: 'str' and 'str' - нельзя делить строку на строку
print('Result:', int(num1) / int(num2)) # num1 = 3 num2 = 3 - Result: 1.0
print('Result:', round(int(num1) / int(num2))) # num1 = 3 num2 = 3 - Result: 1

# или сразу преобразовываем получаемые данные от пользователя к числу
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print('Result:', num1 + num2) # num1 = 3  num2 = 3 - Result: 6
print('Result:', num1 / num2) # num1 = 3  num2 = 3 - Result: 1.0


# Python является языком с динамической типизацией. А это значит, что переменная не привязана жестко с определенному типу.
# В процессе работы программы мы можем изменить тип переменной, присвоив ей значение другого типа
# С помощью встроенной функции type() динамически можно узнать текущий тип переменной
userId = "abc"      # тип str
print(type(userId)) # <class 'str'>
 
userId = 234        # тип int
print(type(userId)) # <class 'int'>