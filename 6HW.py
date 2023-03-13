import random
# Задача 1
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1, n, d = int(input('a1: ')), int(input('n: ')), int(input('d: '))
result = []
for i in range(1, n + 1):
    result.append(d * (i - 1) + a1)
print(result)

# Задача 2
# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
#и не больше заданного максимума)

mylist = [random.randint(-10, 10) for _ in range(int(input('Введите кол-во элементов массива: ')))]
mylist_of_index = []
min, max = int(input('Укажите значение min: ')), int(input('Укажите значение max: '))
print(f'min {min}, max {max}, поиск в массиве {mylist}')
for item in mylist:
    if  min <= item <= max:
        mylist_of_index.append(mylist.index(item))
print(f'заданным условиям принадлежать эллементы под следующими индексами {mylist_of_index}')