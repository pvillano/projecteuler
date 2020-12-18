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
    count_in = count_out = False
    for a, b in ((x, y), (x, y+width-1), (x+width-1, y), (x+width-1, y+width-1)):
        if (a - w_2) ** 2 + (b - w_2) ** 2 <= w_4:
            count_in = True
        else:
            count_out = True
        if count_in and count_out:
            if width == 2:
                return 9
            tot = 0
            width //= 2
            if x == y:
                tot += recurse(x, y, width)
                tot += 2 * recurse(x+width, y, width)
                tot += recurse(x+width, y+width, width)
            else:
                for c, d in ((x, y), (x, y+width), (x+width, y), (x+width, y+width)):
                    tot += recurse(c, d, width)
            return tot + 1
    return 2

def sol():
    return recurse(0,0,w//2) + 2 * recurse(w//2,0,w//2) + recurse(w//2,w//2,w//2) + 1

start_time = time.time()
ans = sol()
d_time = time.time() - start_time
print(n, 1221292, ans,  ans == 1221292)

print(d_time)

# 0.955
# .72
# .69
# .474
# .465
# .445
# .432
# .43
# 113.21299576759338