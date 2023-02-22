# 1 По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * 
# N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
n = int(input('введите число: '))
i = 2
fact = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# 2 Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
#  оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

num1 = 1
num2 = 2
n = int(input('введите число: '))
i = 0
while i < n-2:
        sum = num1 + num2
        num1 = num2
        num2 = sum
        i += 1
print(num2)

# prepodavatel
num1 = 0
num2 = 1
fiboSum = 0
count = 2
number = int(input('Vvedite chislo: '))
while fiboSum < number:
        fiboSum = num1 + num2
        num1, num2 = num2, fiboSum
        count += 1
print(count if number == fiboSum else '-1')

# 3 Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает 
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
#  Здесь каждое число – это масса соответствующего арбуза. 
#  Все числа натуральные и не превышают 30000.

import random
import operator
watermelons = {x : random.randint(2, 9) for x in range(random.randint(9, 35))}
print(watermelons)
print('Самый легкий арбуз. № Арбуза/Вес {}'.format(min(watermelons.items(), key=operator.itemgetter(1))))
print('Самый тяжелый арбуз. № Арбуза/Вес {}'.format(min(watermelons.items(), key=operator.itemgetter(1))))

# 4. Уставшие от необычно теплой зимы, жители решили узнать, действительно
#  ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями 
# статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно
# превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

import random
days = int(input('Enter days'))
count = 0
maxCount = 0
for i in range(days):
        temp = random.randint(-5, 5)
        if temp >= 0:
                count += 1
        else:
                count = 0
        print("Температура {} дня равна {}".format(i, temp))       
        if count > maxCount:
                maxCount = count
print("оттепель длилась {} дня/дней".format(maxCount))



