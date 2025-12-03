
banks = []

with open('Day3/input.txt', 'r') as file:
    for line in file:
        bank = []
        for char in line:
            if char != '\n':
                bank.append(int(char))
        banks.append(bank)

n = 0
maxIdx = -1

for bank in banks:
    num = 0
    maxIdx = -1
    for i in range(0, 12):
        if i != 11:
            maxItem = max(enumerate(bank[maxIdx + 1:-(11-i)]), key=lambda x: x[1])
        else:
            maxItem = max(enumerate(bank[maxIdx + 1:]), key=lambda x: x[1])
        maxNum= maxItem[1]
        maxIdx = maxItem[0] + maxIdx + 1
        num += (maxNum * (10**(11-i)))
    n += num

print(n)

