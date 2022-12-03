# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
list = [2, 5, 0.4, 2, 0.94, 5, 0, 0.94, -0.94, -3]
print(list)
i = 0
while i != len(list):
    k = 0
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            list.pop(j)
            list.pop(i)
            k = -1
            break
    i += 1 + k
print(list)
