# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def convert(n):
    if n == ' ':
        return 1
    else:
        return int(n)

with open('file_task_05_1', 'r') as file1:
    dataFile1 = file1.read()
with open('file_task_05_2', 'r') as file2:
    dataFile2 = file2.read()

poly1 = dataFile1.split('+')
poly2 = dataFile2.split('+')

poly1P1 = convert(poly1[0].split('x')[0])
poly1P2 = convert(poly1[1].split('x')[0])
poly2P1 = convert(poly2[0].split('x')[0])
poly2P2 = convert(poly2[1].split('x')[0])

result = f'{poly1P1 + poly2P1}x^2 + {poly1P2 + poly2P2}x'

with open('file_task_05_3', 'w') as file3:
    file3.write(result)
