f = open("1a_real.txt")
r_list = [("one", "o1e"), ("two", "t2o"), ("three", "t3e"), ("four", "f4r"), ("five", "f5e"), ("six", "s6x"), ("seven", "s7n"),
          ("eight", "e8t"), ("nine", "n9e")]

fl = f.readlines()

sol = []
for l in fl:
    for r in r_list:
        l = l.replace(r[0], r[1])

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
