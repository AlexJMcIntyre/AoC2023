file = open("14a_real.txt")
file_lines = file.readlines()


def print_p():
    print(" 0123456789")
    f = 0
    for fy in p:
        print(str(i) + fy)
        f += 1
    print()


def n():
    for fy in range(1, height):  # move everything up
        for fx in range(width):
            if p[fy][fx] == 'O':
                u = 0  # current distance to move up
                while p[fy - (u + 1)][fx] == "." and (fy - (u + 1)) >= 0:  # check above
                    # we can go up further
                    u += 1
                p[fy] = p[fy][:fx] + '.' + p[fy][fx + 1:]
                p[fy - u] = p[fy - u][:fx] + 'O' + p[fy - u][fx + 1:]


def s():
    for fy in range(height - 2, -1, -1):  # move everything down. Height - 1 is top row!!
        for fx in range(width):
            if p[fy][fx] == 'O':
                u = 0  # current distance to move down
                while (fy + (u + 1)) < height:
                    if p[fy + (u + 1)][fx] == ".":  # check below is clear and within range
                        # we can go down further
                        u += 1
                    else:
                        break
                p[fy] = p[fy][:fx] + '.' + p[fy][fx + 1:]
                p[fy + u] = p[fy + u][:fx] + 'O' + p[fy + u][fx + 1:]


def e():
    for fx in range(width - 2, -1, -1):
        for fy in range(height):
            if p[fy][fx] == 'O':
                u = 0  # current distance to move left
                while (fx + u + 1) < width:
                    if p[fy][fx + u + 1] == '.':
                        # we can move further left
                        u += 1
                    else:
                        break
                p[fy] = p[fy][:fx] + '.' + p[fy][fx + 1:]
                p[fy] = p[fy][:fx + u] + 'O' + p[fy][fx + u + 1:]


def w():
    for fx in range(1, width):
        for fy in range(height):
            if p[fy][fx] == 'O':
                u = 0  # current distance to move left
                while (fx - (u + 1)) >= 0:
                    if p[fy][fx - (u + 1)] == '.':
                        # we can move further left
                        u += 1
                    else:
                        break
                p[fy] = p[fy][:fx] + '.' + p[fy][fx + 1:]
                p[fy] = p[fy][:fx - u] + 'O' + p[fy][fx - u + 1:]


def cycle():
    n()
    w()
    s()
    e()


p = []  # platform
for line in file_lines:
    p.append(line.strip())

height = len(p)
width = len(p[0])

i = 0
history = [p.copy()]


t = 1000000000
while i < 1000000000:
    cycle()
    if p not in history:
        history.append(p.copy())
        i += 1
    else:
        break

for c in enumerate(history):
    if c[1] == p:
        j = c[0]
        break

print('repeat between', j, 'and', i)
outcome = history[(i-j) % (t-(i+1)) + j]

score = 0
for y in range(height):
    score += (height - y) * outcome[y].count("O")
print(score)
