from convert_z26 import (ord26, chr26)


def encode(x, k, n):
    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        x = x.lower()

    y = ''
    for count, c in enumerate(x):
        if count == 0:
            y += current_chr((current_ord(c) + k) % n)
        else:
            y += current_chr((current_ord(c) + current_ord(x[count - 1])) % n)

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
    current_k = k
    for count, c in enumerate(y):
        temp = (current_ord(c) - current_k) % n
        x += current_chr(temp)
        current_k = temp

    return x
