# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('введите натуральную степень: '))

def rnd():
    return random.randint(0, 101)

res = str()
for i in range(k, -1, -1):
    if i == 0:
        txt = f'{rnd()} = 0'
        res += txt
    elif i == 1:
        txt = f'{rnd()}*x + '
        res += txt
    else:
        txt = f'{rnd()}*x^{i} + '
        res += txt

with open('file_task04.txt', 'w') as data:
    data.write(res)
