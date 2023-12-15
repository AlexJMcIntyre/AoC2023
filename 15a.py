file = open("15a_real.txt")
file_lines = file.readlines()


def hash(fstep):
    cv = 0  # current value
    for c in fstep:  # character
        cv = ((cv + ord(c)) * 17) % 256
    return cv


init_seq = file_lines[0].split(",")
scores = []
for step in init_seq:
    scores.append(hash(step))
print(sum(scores))
