from convert_z26 import (ord26, chr26)


def encode(x, k, n):
    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        x = x.lower()
    y = ''
    for c in x:
        y += current_chr((current_ord(c) + k) % n)

    if n == 26:
        return y.upper()

    return y


def decode(y, k, n):
    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        y = y.lower()

    x = ''
    for c in y:
        temp = current_ord(c) - k

        x += current_chr(temp % n)

    return x
