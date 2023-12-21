file = open("18_real.txt")
file_lines = file.readlines()

x, y = 0, 0  # cartesian co-ords this time, just to be confusing
vc = []  # visited co-ordinates
circumference = 2  # initial 1, plus 4 * 0.25 corners

for instruction in file_lines:
    c = instruction.strip().split(' ')[2]  # direction, repeats, colour
    r = int(c[2:7], 16)
    d = c[7]
    circumference += r
    if d == '0':  # Right
        x += r
    if d == '2':  # left
        x -= r
    if d == '1':  # Down
        y -= r
    if d == '3':  # Up
        y += r
    vc.append((x, y))

vc.reverse()
for v in vc:
    print(v[0], ",", v[1])

left, right = 0, 0
r = len(vc)
for i in range(r):
    left += (vc[i][0] * vc[(i+1) % r][1])
    right += (vc[i][1] * vc[(i+1) % r][0])

print((left-right)/2 + (circumference/2))
