import random
#
# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict)
# for key in myDict:
#     print(key)    # пробегаемся по ключам

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict)
# for i in myDict.values():   # использую функцию "values()"
#     print(i)     # пробегаемся по значениям в словаре. 

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict)
# for i in myDict.keys():  # использую функцию 'keys()'
#     print(i)         # проходим по ключам

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict)
# for i in myDict.items():  # использую функцию 'items()'
#     print(i)   # Проходим по ключу и по значению . вывод типа картедж (ключ, знаечние)

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict)
# for i, j in myDict.items():  # использую функцию 'items()'проходимся сразу по двум значениям
#     print(i, j)  # сразу открыли кортедж. int and str

# # Задача: Надо найти значения из словаря, котрые есть в списке
# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# myList = ['second', 'thrid']
# for i in myDict.values():
#     if i in myList:
#         print(i)

# Задача: Надо найти значения из словаря, котрые есть в списке и вывести ключ
# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# myList = ['second', 'thrid']
# for i, j in myDict.items():
#     if j in myList:
#         print(i, j)

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict[1])     
# обращаемся по ключу к словарю, не по индексу(в словарях нет). вывод знаечние values

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict[4])   # еслю ключа нет - краш. не использовать, юзать get()

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict.get(4)) # использую фу-ию get(). В случае ошибки порлучаем None без краша

# myDict = {1:'first', 2: 'second', 3: 'thrid'}   # только вывод заглушки не добавляет в словарь
# print(myDict.get(4, 'Такого значения нет')) # заглушка будет выводиться указаанный эллемент в get
# print(myDict.get(2, 'Такого значения нет')) # second    ok
# print(myDict.get(4, 'Такого значения нет')) # заглушка будет выводиться указаанный эллемент в get
# print(myDict.get(1, 'Такого значения нет')) # first    ok

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict)
# myDict[4] = 'fourth'   # добавили новую запись ключ - знаечние
# print(myDict)

# myDict = {1:'first', 2: 'second', 3: 'thrid'}
# print(myDict)
# myDict.setdefault(5, 'five') # dobavit
# myDict.setdefault(2, 'two') # net
# myDict.setdefault(2, 'blabla') # net
# myDict.setdefault(2, 'thrid') # net
# myDict.setdefault(6, 'six') # dobavit
# print(myDict)

#--------------Задачи

#Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов
#  добавляется к символам с помощью постфикса формата _n.
# myList = [1,2,3,4,2,1] => 1 2 3 4 2_2 1_2

# Мой вариант не при всех условиях работает
myList = [1,2,3,4,2,1]
newSetList = list(set(myList))
mylist2 = []
for item in myList:
    if myList.count(item) > 1:
        mylist2.append('{}_{}'.format(item, myList.count(item)))
    else:
        mylist2.append(item)
setMyList2 = list(set(mylist2))
for item in setMyList2:
    mylist2.remove(item)
print(newSetList + mylist2)

# Вариант преподавателя
stringFromUser = input("Введите значения: ")
myDict = {}
for item in stringFromUser:
    myDict[item] = myDict.get(item, 0) + 1
    
    if myDict[item] == 1:
        print(item, end=", ")
    else:
        print(f"{item}_{myDict[item] - 1}", end= ', ')

print(myDict)

# Вариант преподавателя 2
stringFromUser = input("Введите значения: ")
myDict = {}
for i in stringFromUser:
    myDict[i] = myDict.get(i, 0) + 1 
    print( i if myDict.get(i) == 1 else f'{i}_{myDict.get(i) - 1}', end = ', ')
print('\n' + f'{myDict}')   

# 2 
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или 
# символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.

stringSplit = input("Введите слова через пробел: ").split()
count = 0
for item in stringSplit:
    if stringSplit.count(item) == 1:
        count += 1
print(count)


# От преподавателя 
stringSplit = input("Введите слова через пробел: ").split()
setString = set(stringSplit)
print(len(setString))

print(len(set(input("Введите слова через пробел: ").lower().split())))

# 3
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

# не пошло
# enterFromUser = [random.randint(1000, 9999) for _ in range(7)]
# print(enterFromUser)                                                                #1
# newOne = (str(enterFromUser)).replace(input('Введите число для удаления: '), '')    #2
# print(newOne)                                                                       #3

enterFromUser = [random.randint(1000, 9999) for _ in range(7)]
print(enterFromUser)
list2 = []
list3 = []
n = input('Enter number for serch: ')

for item in enterFromUser:
    part = str(item)
    if n in part:
        part = part.replace(n, '')
    list2.append(part)
print(list2)

for item in list2:
    sumItem = sum([(int(i)) for i in item])
    while sumItem > 9:
        sumItem = sum([(int(i)) for i in str(sumItem)]) 
    list3.append(sumItem)
print(list3)
print(set(list3)) 

    









  

