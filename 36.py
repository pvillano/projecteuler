#lol efficiency
def is_palindrome(number, base):
    digits = []
    while number > 0:
        digits += [number % base]
        number //= base
    stigid = digits.copy()
    stigid.reverse()
    return digits == stigid
tot = 0
for i in range(10 ** 6):
    if is_palindrome(i,10) & is_palindrome(i, 2):
        tot += i

print(tot)