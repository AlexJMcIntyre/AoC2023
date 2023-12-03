f = open("3a_real.txt")
fl = f.readlines()

# Load Grid
grid = []
for row in fl:
    row = row.strip()
    grid_row = []
    for char in row:
        grid_row.append(char)
    grid.append(grid_row)

height = len(grid)
width = len(grid[0])

# Remember to access as row, col!
# print(grid[0][0])

parts = []


def check_surrounds(frow, fcol):
    for crow in range(max(frow - 1, 0), min(frow + 1, height - 1) + 1):
        for ccol in range(max(fcol - 1, 0), min(fcol + 1, height - 1) + 1):
            if grid[crow][ccol] == '*':
                return crow, ccol
    return False


for row in enumerate(grid):
    # move across a row and check if it's a number
    current_number = None
    is_connected = False
    number_grid_loc = None
    gear_grid_loc = None
    i = 0
    while i < width:
        #  print('looking at row ' + str(row[0]) + ', column ' + str(i) + ': ' + row[1][i])
        if row[1][i].isnumeric():
            #  is number
            #  add to the current number if any
            if current_number is None:
                number_grid_loc = (row[0], i)
                current_number = int(row[1][i])
            else:
                current_number = current_number * 10 + int(row[1][i])
            #  check if this bit is connected
            check_con = check_surrounds(row[0], i)
            if check_con is not False:
                gear_grid_loc = check_con
                is_connected = True

        else:
            if current_number is not None:
                #  Is Not number
                #  add previous number to the record
                parts.append((current_number, is_connected, number_grid_loc, gear_grid_loc))
                #  clear previous number
                current_number = None
                is_connected = False
                check_con = False
                gear_grid_loc = False

        i += 1  # end of char

    #  end of row
    #  check if we have a part in the buffer at the end of a row:
    if current_number is not None:
        #  add previous number to the record
        parts.append((current_number, is_connected))
        #  clear previous number
        current_number = None
        is_connected = False
        check_con = False
        gear_grid_loc = False

stars = [] #star location, connected loc, value
for p in parts:
    if p[1]:
        stars.append((p[3], p[2], p[0]))

stars.sort()

starlist = []
s_loc = 0
conn_value = 1
s_con_count = 0

for s in stars:
    if s[0] == s_loc:
        conn_value = conn_value * s[2]
        s_con_count += 1
    else:
        starlist.append((s_loc,conn_value,s_con_count))
        s_loc = s[0]
        conn_value = s[2]
        s_con_count = 1
starlist.append((s_loc,conn_value,s_con_count))

starlist.pop(0)

ans = 0
for s in starlist:
    if s[2] == 2:
        ans += s[1]
print(ans)