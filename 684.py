from otqdm import otqdm


def s(n):
    """smallest number with a digit sum of n"""
    nines, remainder = divmod(n, 9)
    return int(str(remainder) + "9"*nines) % 1000000007


def S(k):
    return sum([s(n) % 1000000007 for n in range(1,k+1)]) % 1000000007


fib = [0,1,1]
while len(fib) < 90:
    fib.append(fib[-1] + fib[-2])


tot = 0
for f in otqdm(fib[2:]):
    tot += S(f)
    tot %= 1000000007