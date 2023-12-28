file = open("20_test.txt")
file_lines = file.readlines()

low = 0
high = 0


class FlipFlop:

    # Flip-flop modules(prefix %) are either on or off; they are initially off. If a flip-flop module receives
    # a high pulse, it is ignored and nothing happens.However, if a flip-flop module receives a low pulse, it flips
    # between on and off.If it was off, it turns on and sends a high pulse.If it was on, it turns off and sends a low
    # pulse.

    def __init__(self, c_name, c_outputs):
        self.name = c_name
        self.state = False
        self.outputs = []
        for co in c_outputs:
            self.outputs.append(co)

    def rec_high(self):
        pass  # do nothing

    def rec_low(self):
        if not self.state:
            self.state = True
            self.out_high()
        else:
            self.state = False
            self.out_low()

    def out_high(self):
        global high
        for o in self.outputs:
            stack.append((o, 'high'))
            high += 1
            print(self.name, 'outputs high to', o)

    def out_low(self):
        global low
        for o in self.outputs:
            stack.append((o, 'low'))
            low += 1
            print(self.name, 'outputs low to', o)


class Conjunction:
    # Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected
    # input modules; they initially default to remembering a low pulse for each input. When a pulse is received,
    # the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all
    # inputs, it sends a low pulse; otherwise, it sends a high pulse.
    def __init__(self, c_name, c_outputs):
        self.name = c_name
        self.remembers = 'low'
        self.outputs = []
        for co in c_outputs:
            self.outputs.append(co)

    def rec_high(self):
        self.remembers = 'high'
        self.out_low()

    def rec_low(self):
        self.remembers = 'low'
        self.out_high()

    def out_high(self):
        global high
        for o in self.outputs:
            stack.append((o, 'high'))
            high += 1
            print(self.name, 'outputs high to', o)

    def out_low(self):
        global low
        for o in self.outputs:
            stack.append((o, 'low'))
            low += 1
            print(self.name, 'outputs low to', o)


class Broadcast:
    # There is a single broadcast module (named broadcaster). When it receives a pulse, it sends the same pulse to all
    # of its destination modules.
    def __init__(self, c_name, c_outputs):
        self.name = c_name
        self.remembers = 'low'
        self.outputs = []
        for co in c_outputs:
            self.outputs.append(co)

    def rec_low(self):
        self.out_low()

    def rec_high(self):
        self.out_high()

    def out_high(self):
        global high
        for o in self.outputs:
            stack.append((o, 'high'))
            high += 1
            print(self.name,'outputs high to',o)

    def out_low(self):
        global low
        for o in self.outputs:
            stack.append((o, 'low'))
            low += 1
            print(self.name, 'outputs low to', o)


class Dummy:
    def __init__(self, c_name):
        self.name = c_name

    def rec_low(self):
        pass

    def rec_high(self):
        pass


system = []

for line in file_lines:
    if line[0] == '%':  # flip-flop
        pl = line[1:].strip().split(' -> ')
        name = pl[0]
        outputs = pl[1].split(", ")
        system.append(FlipFlop(name, outputs))
    elif line[0] == '&':  # Conjunction
        pl = line[1:].strip().split(' -> ')
        name = pl[0]
        outputs = pl[1].split(", ")
        system.append(Conjunction(name, outputs))
    elif line.split(' -> ')[0] == 'broadcaster':  # Broadcast
        pl = line.strip().split(' -> ')
        name = pl[0]
        outputs = pl[1].split(", ")
        system.append(Broadcast(name, outputs))

system.append(Dummy('output'))
stack = []


def get_module(f_name):
    for m in system:
        if m.name == f_name:
            return m


for i in range(1):
    get_module('broadcaster').rec_low()  # push the button
    low += 1

    while len(stack) > 0:
        if stack[0][1] == 'low':
            get_module(stack[0][0]).rec_low()
        elif stack[0][1] == 'high':
            get_module(stack[0][0]).rec_high()
        stack.pop(0)
        print('stack is now', stack)
print(low, high)
print(low * high)
