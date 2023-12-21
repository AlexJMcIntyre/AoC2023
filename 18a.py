file = open("18_real.txt")
file_lines = file.readlines()

move_dict = {('L', 'L'): '-', ('L', 'D'): 'F', ('L', 'U'): 'L', ('R', 'R'): '-', ('R', 'D'): '7', ('R', 'U'): 'J', ('D', 'L'): 'J', ('D', 'R'): 'L', ('D', 'D'): '|', ('U', 'L'): '7', ('U', 'R'): 'F', ('U', 'U'): '|'}
boundary_types = {"|": 1, "-": 0, "L": 0.5, "J": -0.5, "7": 0.5, "F": -0.5, "S": 1}


def dig(fi, fd, fs):
    if fi == 1:
        if fs < len(file_lines) - 1:
            fnd = file_lines[int(fs)+1].strip().split(" ")[0]  # need to know next direction
        else:
            fnd = file_lines[0].strip().split(" ")[0] # wrap around to start for final move
        plan[cs[0]][cs[1]] = move_dict[(fd, fnd)]
    else:
        if d in ('U', 'D'):
            plan[cs[0]][cs[1]] = '|'
        if d in ('L', 'R'):
            plan[cs[0]][cs[1]] = '-'


def print_map():
    for y in plan:
        row = ''
        for x in y:
            row += x
        print(row)
    print()


def expand_map(fd):
    if fd == 'R':
        for y in plan:
            y.append('.')
    elif fd == 'L':
        for y in plan:
            y.insert(0, '.')
        cs[1] += 1
    elif fd == 'D':
        row = []
        for fi in range(len(plan[0])):
            row.append('.')
        plan.append(row)
    elif fd == 'U':
        row = []
        for fi in range(len(plan[0])):
            row.append('.')
        plan.insert(0, row)
        cs[0] += 1


plan = [['#']]  # small initial map
cs = [0, 0]  # the grid. Using (down, right) co-ords !

for instruction in enumerate(file_lines):
    s = instruction[0]  # step
    d, r, c = instruction[1].strip().split(' ')  # direction, repeats, colour
    for i in range(int(r), 0, -1):
        if d == 'R':
            if cs[1] + 1 >= len(plan[0]):
                expand_map(d)
            cs[1] += 1
        if d == 'L':
            if cs[1] - 1 < 0:
                expand_map(d)
            cs[1] -= 1
        if d == 'D':
            if cs[0] + 1 >= len(plan):
                expand_map(d)
            cs[0] += 1
        if d == 'U':
            if cs[0] - 1 < 0:
                expand_map(d)
            cs[0] -= 1
        dig(i, d, s)

# print_map()

score = 0
for y in range(len(plan)):
    boundaries = 0
    for x in range(len(plan[0])):
        t = plan[y][x]
        if not t == '.':
            score += 1
            boundaries += boundary_types[t]
        else:
            if not boundaries % 2 == 0:
                score += 1
                plan[y][x] = '#'
print(score)