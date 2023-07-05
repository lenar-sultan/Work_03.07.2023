# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random

# def find_index(arr, min_value, max_value):
#     index = []
#     for i in range(len(arr)):
#         if min_value <= arr[i] <= max_value:
#             index.append(i)
#     return index


# my_list = [random.randint(1, 10) for _ in range(20)]
# min_Value = int(input("Введите минимальное значение диапазона: "))
# max_Value = int(input("Введите максимальное значение диапазона: "))

# result = find_index(my_list, min_Value, max_Value)
# print(result)  


# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го 
# члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# a1 = int(input("Введите первый элемент:"))
# d = int(input("Введите разность:"))
# n = int(input("Введите количество элементов:"))

# progress = []
# for i in range(n):
#     progress.append(a1 + (i * d))
# print(progress)