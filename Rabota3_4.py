# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('Введите число: '))
k = ''
while n > 0:
    k = str(n % 2) + k
    n = n // 2
print(k)

