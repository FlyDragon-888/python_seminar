# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Введите число")
n = int(input())
pr = []
d = 2
while d * d <= n:
    if n % d == 0:
        pr.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    pr.append(n)
print(pr)