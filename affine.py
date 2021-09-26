from math import gcd

from convert_z26 import (ord26, chr26)
from euclid_mo_rong import tim_phan_tu_nghich_dao


def check_key(k, n):
    if gcd(k[0], k[1]) != 1 or k[0] > k[1] or k[1] > n - 1:
        return False

    return True


def encode(x, k, n):
    if check_key(k, n) == False:
        return "Khoa k khong hop le!"

    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        x = x.lower()

    y = ''
    for c in x:
        y += current_chr((current_ord(c) * k[0] + k[1]) % n)

    if n == 26:
        return y.upper()

    return y


def decode(y, k, n):
    if check_key(k, n) == False:
        return "Khoa k khong hop le!"

    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        y = y.lower()

    nd = tim_phan_tu_nghich_dao(k[0], n)
    x = ''
    for c in y:
        temp = nd * (current_ord(c) - k[1])
        x += current_chr(temp % n)
    return x
