file = open("14a_real.txt")
file_lines = file.readlines()


def print_p():
    for y in p:
        print(y)
    print()


p = []  # platform
for line in file_lines:
    p.append(line.strip())

height = len(p)
width = len(p[0])

for y in range(1, height):  # move everything up
    for x in range(width):
        if p[y][x] == 'O':
            u = 0  # current distance to move up
            while p[y-(u+1)][x] == "." and (y-(u+1)) >= 0:
                # we can go up further
                u += 1
            p[y] = p[y][:x] + '.' + p[y][x + 1:]
            p[y-u] = p[y-u][:x] + 'O' + p[y-u][x + 1:]

score = 0
for y in range(height):
    score += (height - y) * p[y].count("O")
print(score)
