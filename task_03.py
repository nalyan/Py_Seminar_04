# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
list = [2, 5, 4, 2, 5, 0, 5, -3]
i = 0
rep = []
while i != len(list):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            rep.extend([list[i], list[j]])
            break
    i += 1
print(list)

for i in rep:
    if any([elem in list for elem in rep]):
        list.remove(i)
print(list)
