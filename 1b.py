f = open("1a_real.txt")
print(type(f))

r_list = [("one", "o1ne"), ("two", "t2wo"), ("three", "t3hree"), ("four", "f4our"), ("five", "f5ive"), ("six", "s6ix"), ("seven", "s7even"),
          ("eight", "e8ight"), ("nine", "n9ine")]

fl = f.readlines()

sol = []
for l in fl:
    print(l)
    for r in r_list:
        l = l.replace(r[0], r[1])
    print(l)

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
