toword = {0: "",
          1: "one",
          2: "two",
          3: "three",
          4: "four",
          5: "five",
          6: "six",
          7: "seven",
          8: "eight",
          9: "nine",
          10: "ten",
          11: "eleven",
          12: "twelve",
          13: "thirteen",
          14: "fourteen",
          15: "fifteen",
          16: "sixteen",
          17: "seventeen",
          18: "eighteen",
          19: "nineteen",
          20: "twenty",
          30: "thirty",
          40: "forty",
          50: "fifty",
          60: "sixty",
          70: "seventy",
          80: "eighty",
          90: "ninety"}

total = 0
# numbers ending in teens
total += sum([len(toword[i]) for i in range(20)]) * 10
# numbers with 20-90
total += sum([len(toword[i]) for i in range(20,100,10)]) * 100
# last digit of numbers with 20-90
total += sum([len(toword[i]) for i in range(10)]) * 80

# word before hundred
total += sum([len(toword[i]) for i in range(10)]) * 100
total += len("hundred") * (999 - 100 + 1)
total += len("and") * 99 * 9
total += len("onethousand")
print(total)
