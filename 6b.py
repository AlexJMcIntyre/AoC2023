file = open("6a_real.txt")
file_lines = file.readlines()

time = int(file_lines[0].replace(" ", "").strip().split(":")[1])
distance_record = int(file_lines[1].replace(" ", "").strip().split(":")[1])

ways = 0
for hold in range(time + 1):
    # hold = hold time and also speed!
    travel_time = time - hold
    distance_travelled = hold * travel_time
    if distance_travelled > distance_record:
        ways += 1

print(ways)
