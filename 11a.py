file = open("11a_real.txt")
file_lines = file.readlines()

stars = []
for y in file_lines:
    row = []
    for x in y.strip():
        row.append(x)
    stars.append(row)

height = len(stars)
width = len(stars[0])

extra_rows = []
for y in enumerate(stars):
    if '#' not in y[1]:
        extra_rows.append(y[0])

extra_cols = []
for x in range(width):
    append = True
    for y in range(height):
        if stars[y][x] == '#':
            append = False
    if append:
        extra_cols.append(x)

c = []
for y in enumerate(stars):
    for x in enumerate(y[1]):
        if x[1] == '#':
            c.append((y[0], x[0]))

diff = []
for s1 in enumerate(c):
    for s2 in enumerate(c):
        if s1[0] < s2[0]:
            x1, x2 = s1[1][1], s2[1][1]
            y1, y2 = s1[1][0], s2[1][0]
            d = abs(x1 - x2) + abs(y1 - y2)
            for xe in extra_cols:
                if x1 < xe < x2 or x2 < xe < x1:
                    d += 1
            for ye in extra_rows:
                if y1 < ye < y2 or y2 < ye < y1:
                    d += 1
            diff.append(d)
print(sum(diff))
