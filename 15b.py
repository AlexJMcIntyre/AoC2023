import re

file = open("15a_real.txt")
file_lines = file.readlines()


def hash(fstep):
    cv = 0  # current value
    for c in fstep:  # character
        cv = ((cv + ord(c)) * 17) % 256
    return cv


init_seq = file_lines[0].split(",")

boxes = []
for i in range(256):
    boxes.append([])

for step in init_seq:
    pattern = r'[-=]'
    label = re.split(pattern, step)[0]
    cbox = hash(label)  # correct box
    operation = step[len(label)]
    fl = step[len(label)+1:]  # focal length

    if operation == '-':
        # find and remove
        boxes[cbox] = [b for b in boxes[cbox] if label not in b]
    elif operation == '=':
        # check all boxes for matching label
        match = False
        for b in boxes[cbox]:
            if label in b:
                match = True
        if match:  # already a lens in the box with the same label?
            for b in enumerate(boxes[cbox]):
                if label in b[1]:
                    boxes[cbox][b[0]] = label + ' ' + fl
        else:
            # no box with same label
            boxes[cbox].append(label + ' ' + fl)

score = []
for b in enumerate(boxes):
    for e in enumerate(b[1]):
        score.append((b[0] + 1) * (e[0] + 1) * int(e[1].split(" ")[1]))

print(sum(score))


