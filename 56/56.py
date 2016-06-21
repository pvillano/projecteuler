lower_bound = 1
upper_bound = 100
best = 0
for i in range(lower_bound, upper_bound):
    for j in range(lower_bound, upper_bound):
        str_rep = str(i ** j)
        tot = 0
        for digit in str_rep:
            tot += int(digit)
        print(i,"**",j,":",tot)
        best = max(tot, best)
        print(i,"**",j,":",tot)
print(best)
