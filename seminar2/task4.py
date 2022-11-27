# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

print("Введите число")
n = int(input())
a = []
for i in range(-n, n + 1):
    a.append(i)
print(a)
f = open('file.txt', 'r')
p = 1
r = False
for i in f:
    if int(i) < len(a):
        p *= a[int(i)]
        r = True
    else:
        print("Позиция ", i, " отсутсвтует в списке элемнтов")
if r:
    print(p)
f.close()