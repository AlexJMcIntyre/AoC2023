file = open("21a_real.txt")
file_lines = file.readlines()


def get_tile(fx, fy):
    return elf_map[fx + (fy * width)]


def flip_tile(fx, fy):
    if elf_map[fx + (fy * width)] in ('S', 'O'):
        elf_map[fx + (fy * width)] = '.'
    elif elf_map[fx + (fy * width)] == '.':
        elf_map[fx + (fy * width)] = 'O'


def print_map():
    for fy in range(height):
        start = fy * width
        end = start + width
        m_str = ''
        for c in elf_map[start:end]:
            m_str += c
        print(m_str)
    print()


height = len(file_lines)
width = len(file_lines[0].strip())

elf_map = []
for line in file_lines:
    elf_map += [*line.strip()]

for steps in range(64):
    to_flip = []
    for x in range(width):
        for y in range(height):
            if get_tile(x, y) in ('S', 'O'):
                if (x - 1) >= 0 and (x - 1, y) not in to_flip:
                    to_flip.append((x - 1, y))
                if (x + 1) <= width and (x + 1, y) not in to_flip:
                    to_flip.append((x + 1, y))
                if (y - 1) >= 0 and (x, y - 1) not in to_flip:
                    to_flip.append((x, y - 1))
                if (y + 1) <= height and (x, y + 1) not in to_flip:
                    to_flip.append((x, y + 1))
                flip_tile(x, y)
    for f in to_flip:
        flip_tile(f[0], f[1])

print_map()
print(elf_map.count('O'))
