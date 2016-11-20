from math import ceil
squaresSet = None
sqrt = None
def tripletSum(n):
    global squaresSet
    squaresSet = frozenset([i * i for i in range(ceil(n/2))])
    global sqrt
    sqrt = dict([(i * i, i) for i in range(ceil(n/2))])
    for i in range(ceil(n/2)):
        for j in range(i, ceil(n/2)):
            if i**2 + j**2 in squaresSet:
                k = sqrt[i**2 + j**2]
                if i + j + k == n:
                    print(i,j,k, i * j * k)

print(tripletSum(12))
print(tripletSum(1000))