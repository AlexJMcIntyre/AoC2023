file = open("17a_real.txt")
file_lines = file.readlines()


class Block:
    def __init__(self, cx, cy, ch, cp):
        self.x = cx
        self.y = cy
        self.h = int(ch)  # heat loss
        self.p = cp  # 3d plane
        self.n = []  # neighbours (x, y, dist)
        self.d = 1000
        self.v = False
        self.pre = None

    def find_neighbours(self):
        print('finding neighbours for',self)
        if self.p == 'v':
            # we're in the vertical plane, next move must be horizontal
            dist = 0
            for dx in range(1, 4, 1):
                if not 0 <= (self.x + dx) <= width - 1:
                    break
                tp = find_blocks(self.x + dx, self.y, 'h')
                dist += tp.h
                self.n.append((tp, dist))
            dist = 0
            for dx in range(-1, -4, -1):
                if not 0 <= (self.x + dx) <= width - 1:
                    break
                tp = find_blocks(self.x + dx, self.y, 'h')
                dist += tp.h
                self.n.append((tp, dist))

        else:
            # we're in the horizontal plane, next move must be vertical
            dist = 0
            for dy in range(1, 4, 1):
                if not 0 <= (self.y + dy) <= height - 1:
                    break
                tp = find_blocks(self.x, self.y + dy, 'v')
                dist += tp.h
                self.n.append((tp, dist))
            dist = 0
            for dy in range(-1, -4, -1):
                if not 0 <= (self.y + dy) <= height - 1:
                    break
                tp = find_blocks(self.x, self.y + dy, 'v')
                dist += tp.h
                self.n.append((tp, dist))

    def __repr__(self):
        return str(self.h) + ' @ (' + str(self.x) + ', ' + str(self.y) + ', ' + self.p + ')'


def find_blocks(fx, fy, fp):
    for fb in city:
        if fb.x == fx and fb.y == fy and fb.p == fp:
            return fb


def target_reached():
    for fb in target_blocks:
        if fb.v:
            return True


height = len(file_lines)
width = len(file_lines[0].strip())
city = []

for row in enumerate(file_lines):  # load the city
    for col in enumerate(row[1].strip()):
        for p in ('h', 'v'):
            city.append(Block(col[0], row[0], col[1], p))

for b in city:  # create neighbours edges and lengths
    b.find_neighbours()

target_blocks = []
for p in ('h', 'v'):  # set up starting block on all plains
    find_blocks(0, 0, p).d = 0
    target_blocks.append(find_blocks(width - 1, height - 1, p))


def city_sort(c):
    return c.d


i = 0
while not target_reached():
    print('walking through', i, 'of', height*width*2)
    city.sort(key=city_sort)
    cn = [b for b in city if not b.v][0]
    for n in cn.n:  # for each neighbour
        if cn.d + n[1] < n[0].d:  # if current node dist + edge < existing neighbour dist
            n[0].d = cn.d + n[1]  # mark the smaller distance
            n[0].pre = cn
    cn.v = True
    i += 1

sol = []
for t in target_blocks:  # show target results
    sol.append(t.d)

print(min(sol))
