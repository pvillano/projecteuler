# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one
# followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
import speedwatch


def problem56(upper_bound):
    lower_bound = 1
    best = 0
    for i in range(lower_bound, upper_bound):
        for j in range(lower_bound, upper_bound):
            str_rep = str(i ** j)
            tot = 0
            for digit in str_rep:
                tot += int(digit)
            best = max(tot, best)
    return best


speedwatch.watch_time(problem56, range(10, 101, 10))
