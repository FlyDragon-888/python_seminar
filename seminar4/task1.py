# 1. Вычислить число Пи c заданной точностью d
# Пример:
#     - при d = 0.0001,  π = 3.1415    10^-10 ≤ d ≤10^-1
pi = 3.141592653589793
print("Введите точность d числа Пи в диапазоне 10^-10 ≤ d ≤10^-1")
d = input()
if 10**(-10) <= float(d) <= 10**(-1):
    print(str(round(pi,len(d.split('.')[1]) + 1))[:-1])
else:
    print("Точность не соответствует диапазону 10^-10 ≤ d ≤10^-1")