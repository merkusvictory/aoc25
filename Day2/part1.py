ranges = []
with open('Day2/input.txt', 'r') as file:
    for line in file:
        inputs = line.split(',')
        for input in inputs:
            ranges.append(input)

n = 0

for ranged in ranges:
    print(ranged)
    input = ranged.split("-")
    start = int(input[0])
    end = int(input[1])
    for i in range(start, end + 1):
        i_string = str(i)
        first_half = i_string[0:len(i_string)//2]
        second_half = i_string[len(i_string)//2:]
        if first_half == second_half:
            n += i

print(n)
