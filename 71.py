# given 3/7 and denominator d, the largest numerator n such that n/d < 3/7 == 7n < 3d --> n = 3d//7
best_val = 0
best_d = 1
for d in range(8, 1000000):
    if (d % 7 != 0) & (((3 * d) // 7) / d > best_val):
        best_val = ((3 * d) // 7) / d
        best_d = d
        print(d)

best_n = ((3 * best_d) // 7)
i = 1
while i < (best_n ** .05):
    if (best_n % i == 0) & (best_d % i == 0):
        best_n //= i
        best_d //= i
        i += 1
print(best_n, "/", best_d)
