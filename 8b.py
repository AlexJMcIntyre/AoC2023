import math

file = open("8a_real.txt")
file_lines = file.readlines()


class MapNode:
    def __init__(self, input_string):
        input_string = input_string.replace(" =", "").replace("(", "").replace(")", "").replace(",", "").strip().split(" ")
        self.this_node = input_string[0]
        self.left_node = input_string[1]
        self.right_node = input_string[2]


directions = file_lines[0].strip()
map_list = []


def get_map(sm):
    for m in map_list:
        if m.this_node == sm:
            return m


for line in file_lines[2:]:
    map_list.append(MapNode(line))

current_nodes = []
for m in map_list:
    if m.this_node[2] == "A":
        current_nodes.append(m.this_node)


res = []
for current_node in current_nodes:
    steps = 0
    while current_node[2] != "Z":
        if directions[steps % len(directions)] == "L":
            current_node = get_map(current_node).left_node
        else:
            current_node = get_map(current_node).right_node
        steps += 1
    res.append(steps)

print(math.lcm(*res))
