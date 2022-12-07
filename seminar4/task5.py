# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
# *Доп задание: для разного размера уравнения

def getk (y):
    if y[0] == '-':
        maxn = y[1]
        zn = -1
        n = 2
    else:
        maxn = y[0]
        zn = 1
        n = 1
    if maxn.isdigit():
        maxn = 0
        ky = [zn * int(maxn)]
    elif y[-1:] == 'x':
        maxn = 1
        ky = [zn * int(y[:-1])]
    else:
        maxn = maxn.split('x^')
        ky = [zn * int(maxn[0])]
        maxn = int(maxn[1])
    j = 1
    for i in range(n, len(y)):
        k = y[i]
        if k == '+':
            zn = 1
            continue
        elif k == '-':
            zn = -1
            continue
        elif k.isdigit():
            while j != maxn:
                j += 1
                ky.append(0)
            ky.append(zn * int(k))
        elif k[-1:] == 'x':
            while j != maxn - 1:
                j += 1
                ky.append(0)
            ky.append(zn * int(k[:-1]))
        else:
            k = k.split('x^')
            while j != maxn - int(k[1]):
                j += 1
                ky.append(0)
            ky.append(zn * int(k[0]))
        j += 1
    return ky

with open('text1.txt') as f:
    y1 = str(f.readlines())
print(y1[2:-2])
with open('text2.txt') as f:
    y2 = str(f.readlines())
print(y2[2:-2])
y1 = y1[2:-6].split(' ')
y2 = y2[2:-6].split(' ')
ky1 = getk(y1)
ky2 = getk(y2)
if len(ky1) > len(ky2):
    maxk = ky1
    mink = ky2
else:
    maxk = ky2
    mink = ky1
result = []
for i in range(len(maxk)):
    if i >= len(maxk) - len(mink):
        result.append(mink[i - 2] + maxk[i])
    else:
        result.append(maxk[i])

k = len(result) - 1
y = ''
znak = ''
for i in range(k + 1):
    n = result[i]
    if n == 0:
        continue
    if n < 0:
        znak = ' - '
        n = abs(n)
    if k - i == 1:
        y += znak + str(n) + 'x'
    elif k - i == 0:
        y += znak + str(n)
    else:
        y += znak + str(n) + 'x^'+ str(k - i)
    znak = ' + '
y += ' = 0'
f = open('result.txt', 'w')
f.write(y)
f.close()
print(y)