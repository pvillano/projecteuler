from otqdm import otqdm


def reverse(x: int):
    ret = 0
    while x:
        x, digit = divmod(x,10)
        ret = ret * 10 + digit
    return ret


tot = 0
for num in otqdm(range(10000)):
    i = num
    is_l = True
    num += reverse(num)
    for j in range(52):
        mun = reverse(num)
        if mun == num:
            is_l = False
            break
        num += mun
    if is_l:

        tot += 1
print(tot)



