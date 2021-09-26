from convert_z26 import (ord26, chr26)


def encode(x, pi, n):
    pi_string = str(pi)
    if len(x) != len(pi_string):
        return "Khoa k khong hop le!"

    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        x = x.lower()

    y = ''
    for c in pi_string:
        y += x[int(c) - 1]

    print(y)

    if n == 26:
        return y.upper()

    return y


def decode(y, pi, n):
    pi_string = str(pi)
    if len(y) != len(pi_string):
        return "Khoa k khong hop le!"

    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        y = y.lower()

    x = ''
    for i in range(0, len(y)):
        x += y[pi_string.index(str(i + 1))]
    return x
