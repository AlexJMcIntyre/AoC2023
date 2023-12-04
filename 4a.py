f = open("4a_real.txt")
fl = f.readlines()


class Scratchcard:
    def __init__(self, cname, wn, hn):
        self.wn = wn
        self.hn = hn
        self.cname = cname
        self.copies = 0

    def __str__(self):
        return self.cname

    def count_matches(self):
        m = 0
        s = 0
        for w in self.wn:
            if w in self.hn:
                m += 1
                s = max(1, s * 2)
        return s  # score


cards = []  # list of cards

for l in fl:  # load cards into list
    l = l.replace("  ", " ")
    n = l.split(":")[1]
    wnr = n.split("|")[0].strip().split(" ")
    hnr = n.split("|")[1].strip().split(" ")
    cards.append(Scratchcard(cname=l.split(":")[0].strip(), wn=wnr, hn=hnr))

ans = 0
for c in enumerate(cards):
    res = c[1].count_matches()
    print(c[1].cname + ': ', res)
    ans += res

print(ans)
