# 5. Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)

import time
start_time = time.time()
print("Введите число N для диапазона случайных чисел (0, N)")
k = 0
N = int(input())
R = int((1024 * N * (time.time() - start_time))%N)
print(R)