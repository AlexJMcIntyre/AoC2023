file = open("13a_real.txt")
file_lines = file.readlines()


def check_h(c_mirror, fy):
    top = fy
    bottom = fy + 1
    valid = True
    while top >= 0 and bottom <= len(c_mirror) - 1 and valid:
        if not c_mirror[top] == c_mirror[bottom]:
            valid = False
        top += -1
        bottom += 1
    if valid:
        # print("valid horizontal reflection found between", fy + 1, fy + 2)
        # return (fy + 1) * 100
        return 'h', fy + 1
    else:
        return


def check_v(c_mirror, fx):
    left = fx
    right = fx + 1
    valid = True
    while left >= 0 and right <= len(c_mirror[0]) - 1 and valid:
        lstr = ''
        rstr = ''
        for i in range(len(c_mirror)):
            lstr += c_mirror[i][right]
            rstr += c_mirror[i][left]
        if not lstr == rstr:
            valid = False
        left += -1
        right += 1
    if valid:
        # print("valid Vertical reflection found between", fx + 1, fx + 2)
        return 'v', fx + 1
    else:
        return


def process(c_mirror):
    # pass 1
    solutions = []
    for fy in range(0, len(c_mirror) - 1):  # scan down rows, checking for mirror at fy >< fy +1
        s = check_h(c_mirror, fy)
        if s:
            solutions.append(s)
    for fx in range(len(c_mirror[0])-1):  # scan across cols, checking for mirror at fx >< fx +1
        s = check_v(c_mirror, fx)
        if s:
            solutions.append(s)
    # pass 2
    # got our base solution, now go again ignoring base
    sol2 = []
    for cy in range(len(c_mirror)):  # jiggle the mirror
        for cx in range(len(c_mirror[0])):
            t_mirror = c_mirror.copy()
            if t_mirror[cy][cx] == '.':
                t_mirror[cy] = t_mirror[cy][:cx] + '#' + t_mirror[cy][cx + 1:]
            else:
                t_mirror[cy] = t_mirror[cy][:cx] + '.' + t_mirror[cy][cx + 1:]

            for fy in range(0, len(t_mirror) - 1):  # scan down rows, checking for mirror at fy >< fy +1
                if not (fy+1 == solutions[0][1] and solutions[0][0] == 'h'):
                    s = check_h(t_mirror, fy)
                if s:
                    sol2.append(s)
            for fx in range(len(t_mirror[0]) - 1):  # scan across cols, checking for mirror at fx >< fx +1
                if not (fx+1 == solutions[0][1] and solutions[0][0] == 'v'):
                    s = check_v(t_mirror, fx)
                if s:
                    sol2.append(s)

    if sol2[0][0] == 'h':
        return sol2[0][1] * 100
    else:
        return sol2[0][1]


ans = 0
y = []
for line in file_lines:
    if line.strip() == '':
        # new line
        ans += process(y)
        y = []
    else:
        # continue existing
        y.append(line.strip())
ans += process(y)  # clear the buffer
print(ans)
