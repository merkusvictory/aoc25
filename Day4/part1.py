grid = []

with open('Day4/input.txt', 'r') as file:
    for line in file:
        line = line.strip("\n")
        grid.append(list(line))

n = 0

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        adj = 0
        if col == "@":
            if i != 0 and j != 0:
                if grid[i-1][j-1] == "@":
                    adj += 1
            if i != 0:
                if grid[i-1][j] == "@":
                    adj += 1
            if i != 0 and j != len(row) - 1:
                if grid[i-1][j+1] == "@":
                    adj += 1
            if j != 0:
                if grid[i][j-1] == "@":
                    adj += 1
            if j != len(row) - 1:
                if grid[i][j+1] == "@":
                    adj += 1
            if i != len(row) - 1 and j != 0:
                if grid[i+1][j-1] == "@":
                    adj += 1
            if i != len(row) - 1:
                if grid[i+1][j] == "@":
                    adj += 1
            if i != len(row) - 1 and j != len(row) - 1:
                if grid[i+1][j+1] == "@":
                    adj += 1
            if adj < 4:
                n += 1

print(n)