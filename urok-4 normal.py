# Митягин Сергей
# Урок 4 сложность Normal

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    answer = [1, 1]
    while len(answer) < m:
        next_element = answer[-1] + answer[-2]
        answer.append(next_element)
    return answer[n:m+1]
print(fibonacci(99, 1515))
print(sum(fibonacci(99,1515)))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    lenght = len(origin_list)
    for i in range(lenght):
        for j in range(0, lenght - i - 1):
            if origin_list [j] > origin_list[j + 1]:
                temp = origin_list[j]
                origin_list[j] = origin_list[j + 1]
                origin_list[j + 1] = temp
    return origin_list


origin_list = ([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
result = sort_to_max(origin_list)
print(result)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

import random


def my_own_filter(function, spisok):
    """
    наша функция фильтр принимает в себя функцияю и список,
    фильтрует элементы списка spisok с помощью переданной функции function
    и возвращает отфильтрованный список
    :param function: функция должна принимать аргумент и
    возвращать True либо False, это своего рода условие фильтрации
    :param spisok: какой-либо список, элементы которого
    можно отфильтровать с помощью функции function
    (должны соответсвовать какому-либо условию)
    :return filtered_spisok: отсортированный список,
    состоящий из элементов исходного списка,
    которые подходят под условие
    """
    filtered_spisok = []
    for i in spisok:
        print("берём элемент {} из списка {}".format(i, spisok))
        if function(i) == True:
            print('элемент {} подходит, дообавляем его в фильтрованный список {}'.format(i, filtered_spisok))
            filtered_spisok.append(i)
        else:
            print('элемент {} не подходит'.format(i))

    print('отфильтрованный список: {}'.format(filtered_spisok))

    return filtered_spisok


# создадим список, который нужно фильтровать
my_list = []
for i in range(10):
    my_list.append(random.randint(-10, 10))

print('фильтруемый список {}'.format(my_list))


# зададим условие фильтрации для списка в виде функции
def my_condition(element):
    if element > 0:
        return True
    else:
        return False


# вызываем нашу функцию-аналог filter
result = my_own_filter(my_condition, my_list)
print('ответ: ', result)

# то есть, наша функция my_own_filter нужна для того,
# чтобы применить функцию my_condition ко всем элементам списка my_list

# У четырёхугольника без самопересечений все противоположные стороны попарно равны:AB=CD,BC=DA
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

A1 = [2, 1]
A2 = [3, 5]
A3 = [6, 6]
A4 = [5, 2]

B1 = [1, 1]
B2 = [1, 5]
B3 = [5, 5]
B4 = [5, 1]

# не параллелограмм
C1 = [1, 1]
C2 = [5, 5]
C3 = [1, 5]
C4 = [5, 1]


# Функция проверяет является ли четырехугольник параллелограммом
def is_paral(a1, a2, a3, a4):
    # Определим функцию для проверки косинуса угла
    def cos_angle(b1, b2, b3):
        a = (b1[0] - b2[0]) * (b1[0] - b3[0]) + (b1[1] - b2[1]) * (b1[1] - b3[1])
        b = math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2)
        c = math.sqrt((b1[0] - b3[0]) ** 2 + (b1[1] - b3[1]) ** 2)
        return a / (b * c)

    cos_a1 = cos_angle(a1, a2, a4)
    cos_a2 = cos_angle(a2, a3, a1)
    cos_a3 = cos_angle(a3, a4, a2)
    cos_a4 = cos_angle(a4, a3, a1)

    # проверяем равенство углов и сумму соседних углов,
    # т.е. проверяем свойства параллелограма
    if cos_a1 == cos_a3 and cos_a2 == cos_a4 and (cos_a1 + cos_a2) == 0.0 and (cos_a3 + cos_a4) == 0.0:
        return True
    else:
        return False


print(is_paral(A1, A2, A3, A4))
print(is_paral(B1, B2, B3, B4))
print(is_paral(C1, C2, C3, C4))