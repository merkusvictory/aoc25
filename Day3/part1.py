banks = []

with open('Day3/input.txt', 'r') as file:
    for line in file:
        bank = []
        for char in line:
            if char != '\n':
                bank.append(int(char))
        banks.append(bank)

n = 0

for bank in banks:
    maxNum1= max(bank[:-1])
    maxIdx = bank.index(maxNum1)
    maxNum2 = max(bank[maxIdx + 1:])
    n += maxNum1 * 10 + maxNum2

print(n)

