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

steps = 0
current_node = "AAA"

while current_node != "ZZZ":
    if directions[steps % len(directions)] == "L":
        current_node = get_map(current_node).left_node
    else:
        current_node = get_map(current_node).right_node
    steps += 1

print(steps)