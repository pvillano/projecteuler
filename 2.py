def problem2(n):
    prev = 1
    cur = 2
    total = 0
    while cur <= n:
        total += cur
        nex = cur + prev
        prev = cur + nex
        cur = nex + prev
    return total

def main():
    print(problem2(4000000))

if __name__ == "__main__":
    main()