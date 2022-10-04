# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random 
n = int(input('Введите число: '))
listN =[]
for i in range(n):
    listN.append(random.uniform(0, 10))
    listA=[round(i,2) for i in listN if i%1!=0]
    listB=[round(i%1,2) for i in listN if i%1!=0]
print (listA)
print(max(listB) - min(listB))

