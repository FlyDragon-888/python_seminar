# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
#                 - A (3,6); B (2,1) -> 5,09
#                 - A (7,-5); B (1,-1) -> 7,21

print("Введите координату X точки А")
Ax = int(input())
print("Введите координату Y точки А")
Ay = int(input())
print("Введите координату X точки B")
Bx = int(input())
print("Введите координату Y точки B")
By = int(input())
print(str(round(((Ax - Bx)**2 + (Ay - By)**2 )**0.5, 3))[:-1])