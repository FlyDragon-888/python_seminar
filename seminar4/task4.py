# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#     *Пример:*
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
# *Доп задание: значения коэффициентов от -100 до 100

import random
print("Введите натуральное число")
k = int(input())
y = ''
znak = ''
for i in range(k, -1, -1):
    n = random.randrange(-100, 100 + 1)
    if n == 0:
        continue
    if n < 0:
        znak = ' - '
        n = abs(n)
    if i == 1:
        y += znak + str(n) + 'x'
    elif i == 0:
        y += znak + str(n)
    else:
        y += znak + str(n) + 'x^'+ str(i)
    znak = ' + '
y += ' = 0'
f = open('text.txt', 'w')
f.write(y)
f.close()
print(y)
