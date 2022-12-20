# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Изначальный вариант программы
# print("Введите число")
# n = int(input())
# res = []
# for i in range(1, n + 1):
#     p = 1
#     for j in range(1, i + 1):
#         p *= j
#     res.append(p)
# print(res)

def fact(x):
    p = 1
    for i in range(1, x + 1):
        p *= i
    return p

print("Введите число")
n = int(input())
c = list(i for i in range(1, n + 1))
b = list(map(fact, c))
print(b)