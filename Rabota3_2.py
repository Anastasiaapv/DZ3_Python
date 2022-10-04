# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем как в предыдущем задании).
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random 
num = int(input('Введите число: '))
listA =[]
listB =[]
for i in range(num):
    listA.append(random.randint(0, 10))
for i in range(len(listA)):
    while i < len(listA)/2 and num > len(listA)/2:
        num = num - 1
        a = listA[i] * listA[num]
        listB.append(a)
        i += 1
print(listA)
print(listB)

