f = open("1a_real.txt")
fl = f.readlines()

sol = []
for l in fl:
    a1 = ''
    a2 = ''
    for c in l:
        if c.isnumeric():
            if a1 == '':
                a1 = c
            a2 = c
    sol.append(a1 + a2)

ans = 0
for s in sol:
    ans += int(s)
print(ans)
