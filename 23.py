from numpyutils import sum_proper_divisors_array as sumDivisors

n = 28123

abundantList = [i for i, val in enumerate(sumDivisors(n)) if val > i]
abundantSet = set(abundantList)


def has_abundant_sum(n):
    for i in abundantList:
        if i > n // 2:
            return False
        if n - i in abundantSet:
            return True


print(sum([i for i in range(n) if not has_abundant_sum(i)]))
