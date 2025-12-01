inputs = []

with open('Day1/input.txt', 'r') as file:
    for line in file:
        inputs.append((line[0], int(line[1:])))

n = 50
z = 0

for input in inputs:
    prevn = n
    if input[0] == "L":
        n -= input[1]
    if input[0] == "R":
        n += input[1]
    if n == 0:
        z += 1
    if n > 99:
        prev = n
        n = n % 100
        z += prev // 100
    if n < 0:
        prev = n
        n = n % 100
        z += (abs(prev)+100) // 100
        if prevn == 0:
            z -= 1
    if n == 100:
        n = 0

print(z)

