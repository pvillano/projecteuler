def diffSqrSums(n):
    sumSquares = sum(i * i for i in range(n + 1))
    squareSum = (n * (n + 1) // 2) ** 2
    return squareSum - sumSquares


print(diffSqrSums(10), diffSqrSums(100))
