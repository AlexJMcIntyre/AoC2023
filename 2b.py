f = open("2a_real.txt")
fl = f.readlines()

ans = 0

for game in fl:
    red, green, blue = (0, 0, 0)
    game = game.split(":")
    shows = game[1].split(";")
    for show in shows:
        cols = show.split(",")
        for col in cols:
            col = col.strip().split(" ")
            if col[1] == "red" and int(col[0]) > red:
                red = int(col[0])
            if col[1] == "green" and int(col[0]) > green:
                green = int(col[0])
            if col[1] == "blue" and int(col[0]) > blue:
                blue = int(col[0])
    ans += (red * green * blue)
print(ans)