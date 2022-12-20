def calc_value(n1, n2, znak):
    if znak == '+':
        res = complex(n1) + complex(n2)
    elif znak == '-':
        res = complex(n1) - complex(n2)
    elif znak == '*':
        res = complex(n1) * complex(n2)
    else:
        res = complex(n1) / complex(n2)
    return res