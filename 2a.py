f = open("2a_real.txt")
fl = f.readlines()

ans = 0

for game in fl:
    fail = False
    game = game.split(":")
    shows = game[1].split(";")
    for show in shows:
        cols = show.split(",")
        for col in cols:
            col = col.strip().split(" ")
            if col[1] == "red" and int(col[0]) > 12:
                fail = True
            if col[1] == "green" and int(col[0]) > 13:
                fail = True
            if col[1] == "blue" and int(col[0]) > 14:
                fail = True
    if not fail:
        ans += int(game[0].split(" ")[1])
print(ans)