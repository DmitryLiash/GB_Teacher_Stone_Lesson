# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def degree_founder(value1, value2):
#     if value2 == 1:
#         return value1
#     else:
#         return degree_founder(value1, value2 - 1) * value1
# print(degree_founder(int(input('1 : ')), int(input('2 : '))))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

# def strange_summ(value1, value2):
#     if value2 == 0:
#         return value1
#     elif value1 == 0:
#         return value2
#     else:
#         if value2 > 0:
#             return strange_summ(value1 + 1, value2 - 1)
#         else:
#             return strange_summ(value1 - 1, value2 + 1)
            
# print(strange_summ(int(input('1 : ')), int(input('2 : '))))

def strange_summ(value1, value2):
    if value2 == 0:
        return value1
    elif value1 == 0:
        return value2
    else:
        # return strange_summ(value1 + 1, value2 - 1)   #  если знаечние value2 < 0 error
        if value2 > 0:
            return strange_summ(value1 + 1, value2 - 1)
        else:
            return strange_summ(value1 - 1, value2 + 1)
        
print(strange_summ(int(input('1 : ')), int(input('2 : '))))