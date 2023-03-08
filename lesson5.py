import random
def serch(n = random.randint(1, 100)):
    e = int(input('введите число от 1 до 100: '))
    
    while n != e:
        if e > n:
            print('загаданное число меньше')
            e = int(input('Введите число: '))
        print('загаданное больше')
        e = int(input('Введите число: '))
    print('правильно загаданное ч исло было {}'.format(e))
   
serch()

# быстрая сортировка рекурсия
def sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    menshe = [i for i in array[1:] if i <= pivot]
    bolshe = [i for i in array[1:] if i > pivot]
    return sort(menshe) + [pivot] + sort(bolshe)
print(sort([1, 4, 2, 12, 2, 8, 2, 3, 19]))

# 1. Последовательностью Фибоначчи называется
#  последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibby(value):
    if value == 1:
        return 1
    elif value == 0:
        return 0
    else:
        return fibby(value - 1) + fibby(value - 2)
print(fibby(int(input("enter numbers: "))))

# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# макс оценки - хорошие - 3, 4, 5  мин оценки - плохие - 1, 2
vasili_balls = [random.randint(1, 5) for _ in range(10)]
print(vasili_balls)
for i in range(len(vasili_balls)):
    if vasili_balls[i] >= 3:
        vasili_balls.pop(i)
        vasili_balls.insert(i, (random.randint(1, 2)))
print(vasili_balls)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def found_simple_value(value):  # Метод принимает число и выдает его принадлежность к группе
    n = 2                       # простых или составных, выдача в формате str
    while value % n != 0:
        n += 1
        if n == value:
            return "число {} простое".format(n)
    return "число {} составное".format(value)
print(found_simple_value(int(input('Введите число для иследований: '))))