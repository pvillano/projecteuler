# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
#   n → n/2 (n is even)
#   n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

table = {1:0}
def chainLength(n):
    if n in table:
        return table[n]
    elif n %2 == 0:
        length = 1 + chainLength(n//2)
        table[n] = length
        return length
    else:
        n = 3 * n + 1
        return chainLength(n)

def problem14(n):
    maxLen = 0
    for i in range(1,n):
        if chainLength(i)> maxLen:
            print(i,chainLength(i))
            maxLen = chainLength(i)
    return maxLen