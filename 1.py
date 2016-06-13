def eulerSum( max, delta):
    first = delta
    numElements = (max - 1) / delta
    last = delta * numElements
    return (first + last) * numElements / 2
eulerSum(1000, 5) + eulerSum(1000, 3) - eulerSum(1000, 15)