from itertools import count


for max_digits in count(4):
    n = 1
    max_n = 10**max_digits
    print("max_digits:", max_digits, end=" ")
    times_seen = 0
    for i in count(1):
        n *= 2
        if n > max_n:
            n = (n+5)//10  # try to simulate rounding
        if str(n)[:3] == "123":
            times_seen += 1
            if times_seen == 678910:
                print("p(L,n):", i)
                break


