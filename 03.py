# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

original_list = list(map(int, input("Введите числа:").split()))
print(original_list)
new_list = []
[new_list.append(i) for i in original_list if i not in new_list]
print(new_list)