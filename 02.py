# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число N: "))
a = 2
list = []
old = n
while a <= n:
    if n % a == 0:
        list.append(a)
        n //= a
        a = 2
    else:
        a += 1
print(list)
