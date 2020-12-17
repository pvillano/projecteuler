from sympy import isprime

def rtruncable(p):
    while p > 0:
        if not isprime(p):
            return False
        p //= 10
    return True


l_truncables = [2,3,5,7]

tot = 0

for suffix in l_truncables:
    if rtruncable(suffix):
        tot += suffix
        print(suffix)
    for prefix in range(1,10):
        val = int(str(prefix) + str(suffix))
        if isprime(val):
            l_truncables.append(val)
print()
print(tot - sum((2,3,5,7)))
