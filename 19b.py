file = open("19_real.txt")
file_lines = file.readlines()


class Workflow:
    def __init__(self, c_line):
        self.w_rules = []
        self.name, craw = c_line.strip().split("{")
        for cr in craw[:-1].split(","):
            self.w_rules.append(cr)
        self.w_else = self.w_rules.pop(-1)

    def __repr__(self):
        return self.name


def get_workflow(f_name):  # get a workflow, given a name
    for fw in workflows:
        if fw.name == f_name:
            return fw


workflows = []
for line in file_lines:  # load the lists
    if line.strip() == "":
        break
    else:
        workflows.append(Workflow(line))

ID = 0


class Node:
    def __init__(self, c_parent, c_workflow):
        global ID
        self.ID = ID
        ID += 1
        self.parent = c_parent
        self.rules_followed = []  # conditions followed to get to this node
        self.rules_unfollowed = []  # conditions skipped to get to this node
        self.visited = False
        self.workflow = c_workflow
        self.destination_type = None


graph = []
n = Node(None, get_workflow("in"))  # load the root node into graph
graph.append(n)

while True:
    trav = [g for g in graph if not g.visited]
    if len(trav) == 0:
        break  # we have travelled the whole graph
    else:
        for w in trav:
            not_followed = w.rules_unfollowed.copy()  # keep a running tally of rules not followed
            # for all the rules in the workflow of this node, work out children and add them in
            for r in w.workflow.w_rules:
                # this rule leads to another node, add it to the graph
                rule, destination = r.split(":")
                n = Node(w, get_workflow(destination))
                n.rules_followed = w.rules_followed.copy()  # inherit all parent rules
                n.rules_followed.append(rule)  # and also this rule too.
                n.rules_unfollowed = not_followed.copy()  # inherit parent non-followed rules
                if destination in ("A", "R"):
                    n.visited = True  # don't need to check these termini
                    n.destination_type = destination
                graph.append(n)
                not_followed.append(rule)  # add rule to non-followed list for any subsequent nodes in this workflow

            # added in all rules, now add else condition:
            n = Node(w, get_workflow(w.workflow.w_else))
            n.rules_followed = w.rules_followed.copy()
            n.rules_unfollowed = not_followed.copy()
            if w.workflow.w_else in ("A", "R"):
                n.visited = True  # don't need to check these termini
                n.destination_type = w.workflow.w_else
            graph.append(n)
            w.visited = True


def get_node(f_id):  # get a graph node, given an id
    for fn in graph:
        if fn.ID == f_id:
            return fn


ac = [g for g in graph if g.destination_type == 'A']  # all the accepted termini

score = 0
for a in ac:
    x_min, m_min, a_min, s_min = 1, 1, 1, 1
    x_max, m_max, a_max, s_max = 4000, 4000, 4000, 4000

    for r in a.rules_followed:
        if r[0] == 'x':
            if r[1] == '<':
                x_max = min(int(r[2:]) - 1, x_max)
            elif r[1] == '>':
                x_min = max(int(r[2:]) + 1, x_min)
        elif r[0] == 'm':
            if r[1] == '<':
                m_max = min(int(r[2:]) - 1, m_max)
            elif r[1] == '>':
                m_min = max(int(r[2:]) + 1, m_min)
        elif r[0] == 'a':
            if r[1] == '<':
                a_max = min(int(r[2:]) - 1, a_max)
            elif r[1] == '>':
                a_min = max(int(r[2:]) + 1, a_min)
        elif r[0] == 's':
            if r[1] == '<':
                s_max = min(int(r[2:]) - 1, s_max)
            elif r[1] == '>':
                s_min = max(int(r[2:]) + 1, s_min)

    for r in a.rules_unfollowed:
        if r[0] == 'x':
            if r[1] == '>':
                x_max = min(int(r[2:]), x_max)
            elif r[1] == '<':
                x_min = max(int(r[2:]), x_min)
        elif r[0] == 'm':
            if r[1] == '>':
                m_max = min(int(r[2:]), m_max)
            elif r[1] == '<':
                m_min = max(int(r[2:]), m_min)
        elif r[0] == 'a':
            if r[1] == '>':
                a_max = min(int(r[2:]), a_max)
            elif r[1] == '<':
                a_min = max(int(r[2:]), a_min)
        elif r[0] == 's':
            if r[1] == '>':
                s_max = min(int(r[2:]), s_max)
            elif r[1] == '<':
                s_min = max(int(r[2:]), s_min)

    score += ((x_max - x_min + 1) * (m_max - m_min + 1) * (a_max - a_min + 1) * (s_max - s_min + 1))

print(score)
