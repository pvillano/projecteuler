import time


# for a in range(w):
#     for b in range(w):
#         if (a - w_2) ** 2 + (b - w_2) ** 2 <= w_4:
#             print('#', end="")
#         else:
#             print(".", end="")
#     print()

n = 24
w = 2**n
w_2 = w // 2
w_4 = 2 ** (2 * n - 2)


def recurse(x, y, width):
    if width == 1:
        return 2
    count_in = count_out = 0
    for a, b in ((x, y), (x, y+width-1), (x+width-1, y), (x+width-1, y+width-1)):
        if (a - w_2) ** 2 + (b - w_2) ** 2 <= w_4:
            count_in += 1
        else:
            count_out += 1
        if count_in and count_out or width == w:
            tot = 0
            width //= 2
            for x,y in ((x, y), (x, y+width), (x+width, y), (x+width, y+width)):
                tot += recurse(x, y, width)
            return tot + 1
    return 2

start_time = time.time()
ans = recurse(0,0,w)
print(time.time() - start_time)
print(n, ans)


# 249.242657661438