file = open("19_real.txt")
file_lines = file.readlines()


class Workflow:
    def __init__(self, c_line):
        self.w_rules = []
        self.name, craw = c_line.strip().split("{")
        for r in craw[:-1].split(","):
            self.w_rules.append(r)
        self.w_else = self.w_rules.pop(-1)

    def w_run(self, c_part):
        for r in self.w_rules:
            r_subject = r[0]
            r_operator = r[1]
            r_operand, r_destination = r[2:].split(":")

            if r_subject == 'x':
                w_sub = c_part.x
            elif r_subject == 'm':
                w_sub = c_part.m
            elif r_subject == 'a':
                w_sub = c_part.a
            elif r_subject == 's':
                w_sub = c_part.s

            if r_operator == '<':
                if w_sub < int(r_operand):
                    return r_destination
            elif r_operator == '>':
                if w_sub > int(r_operand):
                    return r_destination
        return self.w_else


class Part:
    def __init__(self, c_line):
        r = c_line.strip().split(",")
        self.x = int(r[0][3:])
        self.m = int(r[1][2:])
        self.a = int(r[2][2:])
        self.s = int(r[3][2:-1])
        self.accepted = False
        self.rejected = False


def get_workflow(f_name):
    for fw in workflows:
        if fw.name == f_name:
            return fw


workflows = []
parts = []
mode = 0
for line in file_lines:
    if line.strip() == "":
        mode = 1
    elif mode == 0:
        workflows.append(Workflow(line))
    else:
        parts.append(Part(line))

for p in parts:
    w = "in"
    while not p.accepted and not p.rejected:
        w = get_workflow(w).w_run(p)
        if w == 'A':
            p.accepted = True
        if w == 'R':
            p.rejected = True

score = 0
for p in parts:
    if p.accepted:
        score = score + p.x + p.m + p.a + p.s
print(score)