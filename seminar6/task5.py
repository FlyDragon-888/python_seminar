## Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

# Изначальный вариант программы
# def DelInt(d):
#     dr = str(d).split('.')
#     return round(d - int(dr[0]), len(dr[1]))
#
# print("Введите список из вещественных чисел через запятую")
# n = input().split(',')
# min1 = DelInt(float(n[0]))
# max1 = min1
# for i in range(1, len(n)):
#     k = DelInt(float(n[i]))
#     if k > max1:
#         max1 = k
#     if k < min1:
#         min1 = k
# print(max1 - min1)

def DelInt(d):
    dr = str(d).split('.')
    return round(d - int(dr[0]), len(dr[1]))

print("Введите список из вещественных чисел через запятую")
n = map(float, input().split(','))
b = list(map(DelInt, n))
print(max(b) - min(b))