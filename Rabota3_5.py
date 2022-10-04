# Задача 5. Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
def fibonacci1(n):
    a, b = 1,- 1
    for i in range(n):
        yield a
        a, b = b, a - b
data1 = list(fibonacci1(n))
def fibonacci2(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
data2 = list(fibonacci2(n))   
print(data1,data2)

