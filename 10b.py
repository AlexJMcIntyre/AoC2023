file = open("10a_real.txt")
file_lines = file.readlines()

height = len(file_lines)
width = len(file_lines[0].strip())

tile_types = {"|": ("n", "s"), "-": ("e", "w"), "L": ("n", "e"), "J": ("n", "w"), "7": ("s", "w"), "F": ("s", "e"),
              ".": (), "S": ("n", "e", "s", "w")}
move_type = {"n": (0, -1), "s": (0, 1), "e": (1, 0), "w": (-1, 0)}
boundary_types = {"|": 1, "-": 0, "L": 0.5, "J": -0.5, "7": 0.5, "F": -0.5, "S": 1}


class Tile:
    def __init__(self, fx, fy, ft):
        self.x = fx
        self.y = fy
        self.t = ft
        self.con = tile_types[ft]
        self.on_loop = False

    def __repr__(self):
        return self.t + ' @ ' + str(self.x) + ',' + str(self.y)


tile_map = []


def get_tile(fx, fy):
    for t in tile_map:
        if t.x == fx and t.y == fy:
            return t


def find_tile(ft):
    for t in tile_map:
        if t.t == ft:
            return t


def reset_path():
    for t in tile_map:
        t.on_loop = False


def print_map():
    for y in range(height):
        row = ''
        for x in range(width):
            tile = get_tile(x, y)
            if tile.on_loop:
                row = row + tile.t
            else:
                row = row + ' '
        print(row)
    print()


for y in enumerate(file_lines):
    for x in enumerate(y[1].strip()):
        tile_map.append(Tile(x[0], y[0], x[1].strip()))


def move(fct, fpt):
    for m in fct.con:
        dx = move_type[m][0]
        dy = move_type[m][1]
        fpm = get_tile(fct.x+dx, fct.y+dy)
        if fpm is not None and fpm.t != '.' and fpt != fpm:
            fct.on_loop = True
            return fpm
        # no neighbours
    return False


start_tile = find_tile('S')
ct = start_tile  # current tile
pt = get_tile(0, 0)  # previous tile, to check we don't go backwards. preload with an arbitrary tile not near S

loop = 0
# try a move
while True:
    nt = move(ct, pt)
    if not nt:
        # dead end
        ct = start_tile
        loop = 0
    loop += 1
    if nt.t == 'S':
        print("Done")
        break
    else:
        pt = ct
        ct = nt

score = 0
for y in range(height):

    boundaries = 0
    for x in range(width):
        t = get_tile(x, y)
        if t.on_loop:
            boundaries += boundary_types[t.t]
        else:
            if not boundaries % 2 == 0:
                score += 1
    print("row", y, "score = ", score)
print(score)
