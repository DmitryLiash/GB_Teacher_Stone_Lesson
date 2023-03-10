### 1 --------------------------------------
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

valueFromUser = input('Введите трехзначную цифру, формата *123* : ')
print('Сумма числа равна {}'.format(int(valueFromUser[0]) + 
int(valueFromUser[1]) + int(valueFromUser[2])))

### 2 ---------------------------------------
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
#  если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

valueTogetherCreate = int(input('Введите сколько сделано журавликов всего: '))
valuePetr = int((valueTogetherCreate / 3) / 2)
valueSergey = valuePetr
valueKate = valuePetr * 4
print('Петр сделал: {} журавликов, Катя сделала: {} журавликов,\
 Сергей сделал: {} журавликов,'.format(valuePetr, valueKate, valueSergey))
print('осуждаю детский труд')

### 3 --------------------------------------------
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом
# называют такой билет с шестизначным номером, где сумма первых трех
# цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
 
valueFromUser = input('Введите номер вашего билета: ')
if len(valueFromUser) == 6:
    firstHalfValue = int(valueFromUser[0]) + int(valueFromUser[1]) + int(valueFromUser[2])
    secondHalfValue = int(valueFromUser[3]) + int(valueFromUser[4]) + int(valueFromUser[5])
    if firstHalfValue == secondHalfValue:
        print('yes')
    else:
        print('no')
else:
    print('Счастливым билетом может быть только билет с шестизначным номером')

### 4-----------------------------------------------
# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input('Введите m: '))
n = int(input('Введите n : '))
k = int(input('Введите колл-во долек: '))
if k % m == 0 or k % n == 0 and k < n * m:
    print('yes')
else:
    print('no')






