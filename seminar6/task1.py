num = '15 + 1 * 2 * 3 / 3 - 5'
print(num)
num = num.split()
while len(num) > 1:
    while '*' in num or '/' in num :
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
        else:
            if '*' in num:
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
    while '+' in num or '-' in num :
        if num.count('+') > 0 and num.count('-') > 0:
            if num.index('-') > num.index('+'):
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
        else:
            if '+' in num:
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
print(num)