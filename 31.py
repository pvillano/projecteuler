


def ways(ascending, total):
    if total == 0:
        return 1
    if len(ascending) == 0:
        return 0
    largest = ascending[-1]
    rest = ascending[:-1]
    return sum([ways(rest, total - i) for i in range(0, total + 1, largest)])


print(ways([1,2,5,10,20,50,100,200], 200))
