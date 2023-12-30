file = open("22a_real.txt")
file_lines = file.readlines()


class Brick:
    def __init__(self, c_line):
        global ID
        self.name = str(ID)
        ID += 1
        co_ords = c_line.strip()
        e1, e2 = co_ords.split('~')
        e1, e2 = e1.split(','), e2.split(',')
        self.occupies = []
        for x in range(int(e1[0]), int(e2[0]) + 1):
            for y in range(int(e1[1]), int(e2[1]) + 1):
                for z in range(int(e1[2]), int(e2[2]) + 1):
                    self.occupies.append([x, y, z])
        self.lowest_level = int(e1[2])
        if self.lowest_level == 1:
            self.settled = True
        else:
            self.settled = False
        self.is_supporting = []
        self.supported_by = []

    def __repr__(self):
        return self.name

    def check_and_move(self):
        for o in self.occupies:
            for b2 in [b2 for b2 in bricks if b2 != self]:
                if [o[0], o[1], o[2] - 1] in b2.occupies:
                    if b2.settled:
                        self.settled = True  # landed on a settled brick, which means we're settled
                        return 1, 'settles on ' + b2.name
                    else:
                        return 0, 'bumps ' + b2.name  # bumped a non-settled brick, leave for now
        # checked below all our spaces for all bricks, so we can move down
        for o in self.occupies:
            o[2] -= 1
        self.lowest_level -= 1
        if self.lowest_level == 1:
            self.settled = True
            return 1, 'settled on ground'
        else:
            self.settled = False
            return 0, 'descends'

    def check_above(self):
        self.is_supporting = []
        for o in self.occupies:
            for b2 in [b2 for b2 in bricks if b2 != self]:
                if [o[0], o[1], o[2] + 1] in b2.occupies and b2 not in self.is_supporting:
                    self.is_supporting.append(b2)
                    b2.supported_by.append(self)


ID = 0
bricks = []
for line in file_lines:
    bricks.append(Brick(line))

unsettled = [b for b in bricks if not b.settled]
unsettled.sort(key=lambda x: x.lowest_level)

while len(unsettled) > 0:  # settle the bricks
    for b in unsettled:
        c = b.check_and_move()
        print(b.name, c[1])
    unsettled = [b for b in bricks if not b.settled]
    unsettled.sort(key=lambda x: x.lowest_level)

for b in bricks:
    b.check_above()  # work out what is supporting what.

to_remove = []
for b in bricks:  # check all bricks for disintegration
    # print(b.name, b.supported_by, b.is_supporting)
    remove = True
    for s in b.is_supporting:
        if len(s.supported_by) == 1:
            print('cannot remove', b, 'because of', s)
            remove = False
    if remove:
        print('CAN remove', b)
        to_remove.append(b)

print(len(to_remove))