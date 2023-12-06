file = open("6a_real.txt")
file_lines = file.readlines()

time = file_lines[0].strip().split(" ")[1:]
distance_record = file_lines[1].strip().split(" ")[1:]

while "" in time:  # strip out double spaces
    time.remove("")
while "" in distance_record:
    distance_record.remove("")

time = [int(x) for x in time]
distance_record = [int(x) for x in distance_record]

races = len(time)

ans = 1
for race in range(races):
    ways = 0
    # print("race ", race)
    for hold in range(time[race] + 1):
        # hold = hold time and also speed!
        travel_time = time[race]-hold
        distance_travelled = hold * travel_time
        if distance_travelled > distance_record[race]:
            ways += 1
    ans = ans * ways

print(ans)
