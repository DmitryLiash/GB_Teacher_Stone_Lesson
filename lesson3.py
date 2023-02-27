#1
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
import random
oldList = [random.randint(1, 10) for _ in range(20)]
sortList = set(oldList)
print(oldList)
print(sortList)
print("В списке встречается {} различных эллементов".format(len(sortList)))


oldList = [random.randint(1, 10) for _ in range(20) ]
newList = []
print(oldList)
for item in oldList:
    if item not in newList:
        newList.append(item)
print(newList)
print(len(newList))

# Задача 2
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
#  на K элементов вправо, K – положительное число
# [1,2,3,4,5,6] => [5,6,1,2,3,4]

myList = [random.randint(1, 30) for _ in range(10)]
print(myList)
k = int(input("Введите число: "))
for i in range(k):
    myList.insert(0, myList.pop(-1))
print(myList)

myList = [random.randint(1, 30) for _ in range(11)]
print(myList)
k = int(input("Введите число: "))
print(myList[k:] + myList[:k])

# 3
# Задаем список из рандомных чисел (рандомной длины),
#  нужно составить новый список только с уникальными значениями
# [1, 3, 1, 5, 6, 9, 2, 5] => [3, 6, 9]

#1-------------------------------------
result = []
myList = [random.randint(1, 6) for _ in range(10)]
print(myList)
#2---------------------------------------
copyList = myList.copy()
setList = list(set(copyList))
print(setList)
#3------------------------------------------
for item in setList:
    copyList.remove(item)
print(copyList)
#4----------------------------------------
unikalPovtorValue = list(set(copyList))
print(unikalPovtorValue)
#5-----------------------------------------
for value in myList:
    if value not in unikalPovtorValue:
            result.append(value)
print(result)    

# решение через словарь от преподавателя 1
#1

myList = [random.randint(1, 6) for _ in range(10)]
myDict = {}
newList = []
print(myList)     
for item in myList:
    myDict[item] = myDict.get(item, 0) + 1
print(myDict)

for key, value in myDict.items():
    if value == 1:
        newList.append(key)
print(newList)

#2
myList = [random.randint(1, 6) for _ in range(10)]
newList = []

for item in myList:
    if myList.count(item) == 1:
        newList.append(item)
print(myList)
print(newList)


    

    
    


