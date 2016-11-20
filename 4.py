def is_palindrome(number):
    digits = list(str(number))
    stigid = digits.copy()
    stigid.reverse()
    return digits == stigid


def largestProductPalindrome(pow10):
    for i in range(pow10 - 1, 1, -1):
        a = i
        b = pow10 - 1
        while a <= b:
            if is_palindrome(a * b):
                best = a * b
                for l in range(min(a, b), pow10):
                    for r in range(l, pow10):
                        if is_palindrome(l * r):
                            best = max(best, l * r)
                return best
            else:
                a += 1
                b -= 1


print(largestProductPalindrome(1000))
