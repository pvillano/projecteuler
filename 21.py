from numpyutils import sum_proper_divisors_array

n = 10000
sd = sum_proper_divisors_array(n)


def amicable(i):
    return (sd[i] < n) and (sd[sd[i]] == i) and (sd[i] != i)


print(sum([i for i in range(n) if amicable(i)]))
