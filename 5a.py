file = open("5a_real.txt")
file_lines = file.readlines()


def map_lookup(lookup_value, lookup_map):
    for m_line in lookup_map:  # destination, source, range
        if int(m_line[1]) <= int(lookup_value) <= int(m_line[1]) + int(m_line[2]):
            return int(lookup_value) + int(m_line[0])-int(m_line[1])
    return int(lookup_value)


seeds = []
seeds_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

active = None

for line in file_lines:
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
        seeds_to_soil.append(line.strip().split(" "))
    if active == 'soil-to-fertilizer':
        soil_to_fertilizer.append(line.strip().split(" "))
    if active == 'fertilizer-to-water':
        fertilizer_to_water.append(line.strip().split(" "))
    if active == 'water-to-light':
        water_to_light.append(line.strip().split(" "))
    if active == 'light-to-temperature':
        light_to_temperature.append(line.strip().split(" "))
    if active == 'temperature-to-humidity':
        temperature_to_humidity.append(line.strip().split(" "))
    if active == 'humidity-to-location':
        humidity_to_location.append(line.strip().split(" "))

ans = 1000000000

for s in seeds:
    soil = map_lookup(s, seeds_to_soil)
    fertilizer = map_lookup(soil, soil_to_fertilizer)
    water = map_lookup(fertilizer, fertilizer_to_water)
    light = map_lookup(water, water_to_light)
    temperature = map_lookup(light, light_to_temperature)
    humidity = map_lookup(temperature, temperature_to_humidity)
    location = map_lookup(humidity, humidity_to_location)
    ans = min(location, ans)
    # print(s, soil, fertilizer, water, light, temperature, humidity, location)

print(ans)
