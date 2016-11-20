def largestPrimeFactor(n):
    i = 2
    while i < n:
        while n % i == 0:
            n//= i
        i += 1
    return n

def main():
    for i in range(20):
        print(i, largestPrimeFactor(i))
    print(largestPrimeFactor(600851475143))

if __name__ == '__main__':
    main()