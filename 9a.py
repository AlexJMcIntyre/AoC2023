file = open("9a_real.txt")
file_lines = file.readlines()


def deeper(s):
    current_depth = len(s[0])-1
    for e in enumerate(s):
        if e[0] <= current_depth:
            e[1].append(None)
        else:
            ct = s[e[0]][-1]  # current element of list segment
            pl = s[e[0]-1][-2]  # penultimate element of last segment
            e[1].append(ct - pl)


def check(s):
    for e in s:
        if e[-1] not in (None, 0):
            return False
    return True


def extrapolate(s):
    return sum(s[-1])


ans = 0
for line in file_lines:
    seq = [[int(x)] for x in line.strip().split(" ")]
    while not check(seq):
        deeper(seq)
    ans += extrapolate(seq)

print(ans)
