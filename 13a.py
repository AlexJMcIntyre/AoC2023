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
    # print_mirror(c_mirror)
    solutions = []
    for fy in range(0, len(c_mirror) - 1):  # scan down rows, checking for mirror at fy >< fy +1
        s = check_h(c_mirror, fy)
        if s:
            solutions.append(s)
    for fx in range(len(c_mirror[0])-1):  # scan across cols, checking for mirror at fx >< fx +1
        s = check_v(c_mirror, fx)
        if s:
            solutions.append(s)
    if solutions[0][0] == 'h':
        return solutions[0][1] * 100
    else:
        return solutions[0][1]


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
