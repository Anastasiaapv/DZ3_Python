# Задача 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
n = int(input('Введите число: '))
listN =[]
for i in range(n):
    listN.append(random.randint(0, 10))
print (listN)
print (sum(listN[1::2]))

