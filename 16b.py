file = open("16a_real.txt")
file_lines = file.readlines()

move_dict = {'u': (0, -1), 'd': (0, 1), 'r': (1, 0), 'l': (-1, 0)}
reflect_dict = {}


class GridSpace:
    def __init__(self, cx, cy, ct):
        self.x = cx
        self.y = cy
        self.t = ct  # tile type
        self.e = False  # energised
        self.d = []  # directions already explored


class Beam:
    def __init__(self, cx, cy, ccd):
        self.x = cx
        self.y = cy
        self.cd = ccd
        self.active = True


def find_gs(fx, fy):  # find a grid space object with given co-ordinates
    for gs in contraption:
        if gs.x == fx and gs.y == fy:
            return gs


def change_dir(fcd, fx, fy):  # change direction based on incoming direction and tile type
    ft = find_gs(fx, fy).t
    if ft == '/' and fcd == 'u':
        return 'r'
    elif ft == '/' and fcd == 'd':
        return 'l'
    elif ft == '/' and fcd == 'l':
        return 'd'
    elif ft == '/' and fcd == 'r':
        return 'u'
    elif ft == '\\' and fcd == 'u':
        return 'l'
    elif ft == '\\' and fcd == 'd':
        return 'r'
    elif ft == '\\' and fcd == 'l':
        return 'u'
    elif ft == '\\' and fcd == 'r':
        return 'd'
    elif ft == '-' and fcd == 'u':
        beams.append(Beam(fx, fy, 'l'))
        return 'r'
    elif ft == '-' and fcd == 'd':
        beams.append(Beam(fx, fy, 'l'))
        return 'r'
    elif ft == '|' and fcd == 'l':
        beams.append(Beam(fx, fy, 'u'))
        return 'd'
    elif ft == '|' and fcd == 'r':
        beams.append(Beam(fx, fy, 'u'))
        return 'd'
    else:
        return fcd


def print_map():
    for fy in range(height):
        row = ''
        for fx in range(width):
            fg = find_gs(fx, fy)
            if fg.e:
                row = row + '#'
            else:
                row = row + fg.t
        print(row)
    print()


def reset():
    for c in contraption:
        c.e = False
        c.d = []


def fire():
    global beams
    while len(beams) > 0:
        for b in beams:
            # move beam into a new space
            b.x += move_dict[b.cd][0]
            b.y += move_dict[b.cd][1]
            if not (0 <= b.x <= width-1 and 0 <= b.y <= height-1):
                # out of bounds
                b.active = False  # flag for removal
                break
            new_tile = find_gs(b.x, b.y)
            if b.cd in new_tile.d:
                # we've explored this direction before
                b.active = False
            else:
                new_tile.e = True
                new_tile.d.append(b.cd)
                # change direction based on mirror in new current space
                b.cd = change_dir(b.cd, b.x, b.y)

        # remove dead beams now we're through the loop
        beams = [be for be in beams if be.active]
    ans = 0
    for g in contraption:
        if g.e:
            ans += 1
    return ans


height = len(file_lines)
width = len(file_lines[0].strip())

contraption = []
for y in enumerate(file_lines):
    for x in enumerate(y[1].strip()):
        contraption.append(GridSpace(x[0], y[0], x[1]))

res = []
for y in range(height):
    print('y =',y)
    beams = [Beam(0, y, change_dir('r', 0, y))]
    find_gs(0, y).e = True
    res.append(fire())
    reset()

for y in range(height):
    print('y =', y)
    beams = [Beam(width-1, y, change_dir('l', width-1, y))]
    find_gs(width-1, y).e = True
    res.append(fire())
    reset()

for x in range(width):
    print('x =', x)
    beams = [Beam(x, 0, change_dir('d', x, 0))]
    find_gs(x, 0).e = True
    res.append(fire())
    reset()

for x in range(width):
    print('x =', x)
    beams = [Beam(x, height-1, change_dir('u', x, height-1))]
    find_gs(x, height-1).e = True
    res.append(fire())
    reset()

print(max(res))


