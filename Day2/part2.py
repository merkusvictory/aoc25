ranges = []
with open('Day2/input.txt', 'r') as file:
    for line in file:
        inputs = line.split(',')
        for input in inputs:
            ranges.append(input)

n = 0

for ranged in ranges:
    input = ranged.split("-")
    start = int(input[0])
    end = int(input[1])
    for i in range(start, end + 1):
        i_string = str(i)
        chain = ""
        for char in i_string:
            valid = True
            chain += char
            if len(chain) != len(i_string):
                for chr in i_string.split(chain):
                    if chr != '':
                        valid = False
                if valid == True:
                    n += i
                    break
                

            

print(n)