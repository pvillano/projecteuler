FAKE_WIDTH = 15
WIDTH = FAKE_WIDTH + 1
diagonal = [0] * WIDTH
diagonal[0] = 1
temp = list(diagonal)
for i in range(WIDTH - 1):
    #temp[0] = 1
    for j in range(	1, WIDTH):
        temp[j] = diagonal[j - 1] + diagonal[j]
    temptemp = temp
    temp = diagonal
    diagonal = temptemp
for i in range(WIDTH - 1):
    temp = [0] * WIDTH
    for j in range(WIDTH - 1):
        temp[j] = diagonal[j] + diagonal[j + 1]
    temp[WIDTH - i - 1] = 0
    diagonal = temp
diagonal