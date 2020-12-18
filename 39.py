from sympy.core.power import integer_nthroot

from otqdm import otqdm

num_solutions = [0] * 1001


def root_if_square(n: int):
    """
    n must be pos (not tested)
    stolen from sympy.ntheory.primetest.s_square
    """
    # if n <= 0:
    #     return False
    if n == 1:
        return 1
    m = n & 127
    if not ((m*0x8bc40d7d) & (m*0xa1e2f5d1) & 0x14020a):
        m = n % 63
        if not ((m*0x3d491df7) & (m*0xc824a9f9) & 0x10f14008):
            root, is_square = integer_nthroot(n, 2)
            if is_square:
                return root
    return False


for a in otqdm(range(1000)):
    for b in range(a, 1000):
        if a+b>1000:
            break
        c2 = a*a + b*b
        if c2 > (1000 - a - b)**2:
            break
        c = root_if_square(c2)
        if c:
            p = a+b+c
            if p < 1000:
                num_solutions[p] += 1
            else:
                break

print(max(enumerate(num_solutions), key=lambda x: x[1]))

