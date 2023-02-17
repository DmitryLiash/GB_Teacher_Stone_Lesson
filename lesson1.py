#ok
import math
kmForDay = 700 # машина проезжает за день
allDistance = 750 # все растояние
result = allDistance / kmForDay
ceil = math.ceil((result))
print(ceil)

#ok
kmForDay = 700 # машина проезжает за день
allDistance = 750 # все растояние
result = (allDistance +  kmForDay - 1) // kmForDay
print(result) 

#ne ok
kmForDay = 700 # машина проезжает за день
allDistance = 750 # все растояние
result = allDistance // kmForDay + 1
print(result) # при кратных значения ошибка + 1 получается

#------------------------------------
# В некоторой школе решили набрать три новых математических 
# класса и оборудовать кабинеты для них новыми партами.
#  За каждой партой может сидеть два учащихся. 
#  Известно количество учащихся в каждом из трех классов.
#   Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20 учен
# 21 учен
# 22 учен
# **Output:**
# 32  парты нужны

#ok
first = 20
second = 21
thrid = 22
result = (20 + 21 + 22) // 2 + (20 + 21 + 22) % 2
print(result)

#ok
first = int(input('введите кол-во ученеков из 1 класса. п.у.з. 20 :'))
second = int(input('введите кол-во ученеков из 1 класса. п.у.з. 21 :'))
thrid = int(input('введите кол-во ученеков из 1 класса. п.у.з. 22 :'))
result = ((20 + 21 + 22) / 2) + 0.5
print(int(result))

#-------------------------------------
#Вагоны в электричке пронумерованы натуральными числами,
#  начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
#  а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
#  В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и
#  обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего
#  вагонов в электричке. Напишите программу, которая будет это делать или
#  сообщать, что без дополнительной информации это сделать невозможно.

#ok
numberCountWagon = int(input('введите порядковый номер вагона от тепловоза:')) 
numberOfWagon = int(input('введите номер вагона :'))
if numberOfWagon != numberCountWagon:
    result = numberCountWagon + numberOfWagon - 1
    print('В поезде {} вагонов'.format(result))
else:
    print('Невозможно посчитать т.к. нумерация поезда идет с головы')

# ----------------------------------------------
# Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# **Input:**
# 2016
# **Output:**
# YES

#ok
value = int(input('Enter year :'))
if value % 4 == 0 and  value % 100 != 0 or value % 400 == 0:
    print('yes')
else:
    print('no')

 


