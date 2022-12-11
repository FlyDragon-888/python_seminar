# 2. Создайте программу для игры в ""Крестики-нолики"".

def printa(a):
    for i in range(3):
        print()
        for j in range(3):
            print(a[i][j] + ' ' , end='')
    print()

a = [['-'] * 3 for i in range(3)]
printa(a)
win = 0
g = 2
while win == 0:
    if g == 1:
        g = 2
        p = '0'
    else:
        g = 1
        p = 'X'
    st = input(f"Ход Игрока №{g}: ").split(',')
    if (0 < int(st[0]) < 4) and (0 < int(st[1]) < 4):
        if a[int(st[0]) - 1][int(st[1]) - 1] == '-':
            a[int(st[0]) - 1][int(st[1]) - 1] = p
            printa(a)

            k = 1
            for i in range(3):
                for j in range(2):
                    if a[i][j] == '-':
                        continue
                    elif a[i][j] == a[i][j + 1]:
                        k += 1
            if k == 3:
                win = 1
            k = 1
            for j in range(3):
                for i in range(2):
                    if a[i][j] == '-':
                        continue
                    elif a[i][j] == a[i + 1][j]:
                        k += 1
            if k == 3:
                win = 1
            k = 1
            for i in range(2):
                if a[i][i] == '-':
                    continue
                elif a[i][i] == a[i + 1][i + 1]:
                    k += 1
            if k == 3:
                win = 1
            for i in range(2):
                if a[i][2 - i] == '-':
                    continue
                elif a[i][2 - i] == a[i + 1][2 - i - 1]:
                    k += 1
            if k == 3:
                win = 1

        else:
            print('Данная позиция уже отмечена, выберите другую')
    else:
        print('Введите два числа от 1 до 3 через запятую. Первое число - номер строки, второе - номер столбца')

print(f'Выиграл Игрок №{g}')