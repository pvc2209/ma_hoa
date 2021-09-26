def tim_phan_tu_nghich_dao(a, n):
    x1 = n
    x2 = a
    b1 = 0
    b2 = 1

    while (x2 != 1):
        y = x1 // x2
        temp_x2 = x2
        x2 = x1 % x2
        x1 = temp_x2

        temp_b2 = b2
        b2 = b1 - (b2 * y)
        b1 = temp_b2

    if b2 < 0:
        return n + b2

    return b2


if __name__ == '__main__':
    result = tim_phan_tu_nghich_dao(21, 1112064)
    print(result)
