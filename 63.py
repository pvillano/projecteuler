#10^n is n + 1 digits
#only need to test 9-- for each power
total = 0
n = 1
while len(str(9**n)) == n:
    for i in range(1, 10):
        if len(str(i**n)) == n:
            #print i, "**", n, " is ", i**n
            total+=1
        
    n+=1
print total