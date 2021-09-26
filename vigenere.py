from convert_z26 import (ord26, chr26)


def encode(x, k, n):
    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        x = x.lower()

    y = ''
    k = k.lower()
    m = len(k)
    for count, c in enumerate(x):
        index = count % m
        y += current_chr((current_ord(c) + current_ord(k[index])) % n)

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
    k = k.lower()
    m = len(k)

    for count, c in enumerate(y):
        index = count % m
        temp = current_ord(c) - current_ord(k[index])

        x += current_chr(temp % n)
    return x
