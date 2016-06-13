import math
PHI = (1 + math.sqrt(5)) / 2
#PHI = 1.61803398875
logPHI = math.log10(PHI)
LAMBDA = 1
DIGITS = 1000
def logError(a, b):
    return (abs(math.log10(a) - math.log10(b)))
 
def approxIsGood( cur, logError):
    #digits left is not a precise name for this non-integer
    curDigits = math.log10(cur) + 1
    if curDigits > DIGITS:
    	return True
    digitsLeft = DIGITS - curDigits
    numIterations = digitsLeft / math.log10(PHI)
    if (abs(logError * numIterations) > LAMBDA):
        return False
    return True

i = 2
cur = 1
prev = 1
while not approxIsGood(cur, logError(float(cur)/prev, PHI)):
    temp = cur
    cur = cur + prev
    prev = temp
    i += 1
 
numDigits = math.log10(cur) + 1
i += int(math.ceil(((DIGITS - numDigits)/logPHI)))
print(i)