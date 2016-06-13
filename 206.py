import math
import re
import sys
minX = int(math.floor(1020304050607080900 ** .5))
maxX = int(math.ceil(1929394959697989990 ** .5))
minX = int(minX / 10) * 10
print(minX)
print(maxX)

pattern = re.compile('1.2.3.4.5.6.7.8.9.0')
i = minX
print(str(i * i))
# if pattern.match(str(1122334455667788990)):
#     print("you not craycray")
# if pattern.match(str(112233445566778899)):
#     print("but python is")
while i < maxX:
    if pattern.match(str(i * i)):
        print(i)
        sys.exit()
    # else:
    #     print(str(i) + "is not a match")
    i += 10
