from convert_z26 import (ord26, chr26)
from euclid_mo_rong import tim_phan_tu_nghich_dao
from math import gcd


def encode(x, k, n):
    if len(k) != 4:
        return "Khoa k khong hop le!"

    if len(x) % 2 != 0:
        x += 'z'

    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        x = x.lower()

    k11 = k[0]
    k12 = k[1]
    k21 = k[2]
    k22 = k[3]

    # k11 k12
    # k21 k22

    y = ''
    for i in range(0, len(x), 2):
        x1 = current_ord(x[i])
        x2 = current_ord(x[i + 1])
        y1 = x1 * k11 + x2 * k21
        y2 = x1 * k12 + x2 * k22

        y += current_chr(y1 % n) + current_chr(y2 % n)

    if n == 26:
        return y.upper()

    return y


def decode(y, k, n):
    # Neu n = 1112064
    # thi k = 7 13
    #         3 9
    # => detk = 17
    # thi ucln(1112064, detk) moi bang 1

    # khi ucln(n, detk) != 1 thì ta vẫn mã hóa được vì trong hàm encode
    # không cần detk

    if len(k) != 4:
        return "Khoa k khong hop le!"

    current_ord = ord
    current_chr = chr

    if n == 26:
        current_ord = ord26
        current_chr = chr26
        y = y.lower()

    # k
    k11 = k[0]
    k12 = k[1]
    k21 = k[2]
    k22 = k[3]

    detk = k11 * k22 - k21 * k12

    if gcd(detk, n) != 1:
        return "Khong ton tai ma tran ND"

    nd = tim_phan_tu_nghich_dao(detk, n)

    # tinh k*
    k_star_11 = k22
    k_star_12 = -k12
    k_star_21 = -k21
    k_star_22 = k11

    # tinh k nghich dao
    knd_11 = (k_star_11 * nd) % n
    knd_12 = (k_star_12 * nd) % n
    knd_21 = (k_star_21 * nd) % n
    knd_22 = (k_star_22 * nd) % n

    x = ''
    for i in range(0, len(y), 2):
        y1 = current_ord(y[i])
        y2 = current_ord(y[i + 1])
        x1 = y1 * knd_11 + y2 * knd_21
        x2 = y1 * knd_12 + y2 * knd_22

        x += current_chr(x1 % n) + current_chr(x2 % n)
    return x
