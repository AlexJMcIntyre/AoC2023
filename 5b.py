file = open("5a_real.txt")
file_lines = file.readlines()


def map_sort_key(map_element):  # a key to sort maps via the source range
    return map_element[1]


def sub_map_lookup(lookup_value, lookup_map):
    lookup_value = int(lookup_value)
    # function needs to return correct mapping and for how many seeds after it is a valid result for
    for m_line in lookup_map:  # check each range in the map. destination, source, range
        source_from = int(m_line[1])
        destination_from = int(m_line[0])
        line_range = int(m_line[2])
        offset = destination_from - source_from
        source_to = source_from + line_range - 1
        if source_from <= int(lookup_value) <= source_to:
            # is offset by this map
            mapped = lookup_value + offset
            extra_range = source_to - lookup_value
            return mapped, extra_range
    # is not offset by this map
    # find start of next-highest range:
    for m_line in lookup_map:  # check each range in the map. destination, source, range
        source_from = int(m_line[1])
        # does this source range start higher than our lookup?
        if source_from > lookup_value:
            # we're higher, return the difference between lookup and range star
            return lookup_value, source_from - lookup_value
    # there is no higher source, return an arbitrarily large range
        return lookup_value, 100000000000


def map_lookup(lookup_value):  # run through all the maps and find the outcome, and lowest valid range
    valid_range = []
    for mxf in m1, m2, m3, m4, m5, m6, m7:
        lookup_result = sub_map_lookup(lookup_value, mxf)
        lookup_value = lookup_result[0]
        valid_range.append(lookup_result[1])
    return lookup_value, min(valid_range)


seeds = []
m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
m6 = []
m7 = []

active = None

for line in file_lines:  # load the source data
    if line.strip() == '':
        continue
    if 'seeds' in line:
        active = 'seeds'
    if 'seed-to-soil' in line:
        active = 'seed-to-soil'
        continue
    if 'soil-to-fertilizer' in line:
        active = 'soil-to-fertilizer'
        continue
    if 'fertilizer-to-water' in line:
        active = 'fertilizer-to-water'
        continue
    if 'water-to-light' in line:
        active = 'water-to-light'
        continue
    if 'light-to-temperature' in line:
        active = 'light-to-temperature'
        continue
    if 'temperature-to-humidity' in line:
        active = 'temperature-to-humidity'
        continue
    if 'humidity-to-location' in line:
        active = 'humidity-to-location'
        continue
    if active == 'seeds':
        seeds = (line.strip().split(" ")[1:])
    if active == 'seed-to-soil':
        m1.append(line.strip().split(" "))
    if active == 'soil-to-fertilizer':
        m2.append(line.strip().split(" "))
    if active == 'fertilizer-to-water':
        m3.append(line.strip().split(" "))
    if active == 'water-to-light':
        m4.append(line.strip().split(" "))
    if active == 'light-to-temperature':
        m5.append(line.strip().split(" "))
    if active == 'temperature-to-humidity':
        m6.append(line.strip().split(" "))
    if active == 'humidity-to-location':
        m7.append(line.strip().split(" "))

# sort the maps by source range
for mx in m1, m2, m3, m4, m5, m6, m7:
    mx.sort(key=map_sort_key)

ans = 100000000000

# calculating seed ranges
for s in range(0, len(seeds) - 1, 2):
    seed_start = int(seeds[s])
    seed_end = seed_start + int(seeds[s+1]) - 1
    seed_i = seed_start
    while seed_i <= seed_end:
        result = map_lookup(seed_i)
        ans = min(result[0], ans)
        seed_i += 1 + result[1]

print(ans)
