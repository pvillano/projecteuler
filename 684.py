from otqdm import otqdm

seen = [1,10]
def mod10(nines):
    while nines >= len(seen):
        seen.append((seen[-1]*10)% 1000000007)
    return seen[nines]


def s(n):
    """smallest number with a digit sum of n"""
    nines, remainder = divmod(n, 9)
    return ((remainder+1) * mod10(nines) - 1) % 1000000007


def S(k):
    tot = 0
    for n in range(1, k + 1):
        tot += s(n)
        tot %= 1000000007
    return tot


fib = [0,1,1]
while len(fib) < 90:
    fib.append(fib[-1] + fib[-2])


tot = 0
for f in otqdm(fib[2:]):
    tot += S(f)
    tot %= 1000000007