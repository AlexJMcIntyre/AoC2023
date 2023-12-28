file = open("20_real.txt")
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

    def rec_high(self, cinput):
        pass  # do nothing

    def rec_low(self, cinput):
        if not self.state:
            self.state = True
            self.out_high()
        else:
            self.state = False
            self.out_low()

    def out_high(self):
        global high
        for o in self.outputs:
            stack.append((o, 'high', self.name))
            high += 1
            print(self.name, '-high->', o)

    def out_low(self):
        global low
        for o in self.outputs:
            stack.append((o, 'low', self.name))
            low += 1
            print(self.name, '-low->', o)


class Conjunction:
    # Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected
    # input modules; they initially default to remembering a low pulse for each input. When a pulse is received,
    # the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all
    # inputs, it sends a low pulse; otherwise, it sends a high pulse.
    def __init__(self, c_name, c_outputs):
        self.name = c_name
        self.inputs = [] # [input name, state]
        self.outputs = []
        for co in c_outputs:
            self.outputs.append(co)

    def rec_high(self, cinput):
        # first record the high for this input
        for ci in self.inputs:
            if ci[0] == cinput:
                ci[1] = 'high'
        # now check all inputs are high, if so output low
        for ci in self.inputs:
            if ci[1] == 'low':
                self.out_high()
                return
        self.out_low()

    def rec_low(self, cinput):
        # first record the low for this input
        for ci in self.inputs:
            if ci[0] == cinput:
                ci[1] = 'low'
        self.out_high()  # we've just recorded a low, so can assume a high output

    def out_high(self):
        global high
        for o in self.outputs:
            stack.append((o, 'high', self.name))
            high += 1
            print(self.name, '-high->', o)

    def out_low(self):
        global low
        for o in self.outputs:
            stack.append((o, 'low', self.name))
            low += 1
            print(self.name, '-low->', o)


class Broadcast:
    # There is a single broadcast module (named broadcaster). When it receives a pulse, it sends the same pulse to all
    # of its destination modules.
    def __init__(self, c_name, c_outputs):
        self.name = c_name
        self.remembers = 'low'
        self.outputs = []
        for co in c_outputs:
            self.outputs.append(co)

    def rec_low(self, cinput):
        self.out_low()

    def rec_high(self, cinput):
        self.out_high()

    def out_high(self):
        global high
        for o in self.outputs:
            stack.append((o, 'high', self.name))
            high += 1
            print(self.name,'-high->',o)

    def out_low(self):
        global low
        for o in self.outputs:
            stack.append((o, 'low', self.name))
            low += 1
            print(self.name, '-low->', o)


class Dummy:
    def __init__(self, c_name):
        self.name = c_name
        self.outputs = []

    def rec_low(self, cinput):
        pass

    def rec_high(self, cinput):
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

system.append(Dummy('rx'))

for s in [s for s in system if type(s).__name__ == 'Conjunction']:
    for i in [i for i in system if s.name in i.outputs]:
        s.inputs.append([i.name, 'low'])

stack = []  # (to, pulse, from)


def get_module(f_name):
    for m in system:
        if m.name == f_name:
            return m


for i in range(1000):
    print('button -low-> broadcaster')
    get_module('broadcaster').rec_low(None)  # push the button
    low += 1

    while len(stack) > 0:
        if stack[0][1] == 'low':
            get_module(stack[0][0]).rec_low(stack[0][2])
        elif stack[0][1] == 'high':
            get_module(stack[0][0]).rec_high(stack[0][2])
        stack.pop(0)
        # print('stack is now', stack)

print(low, high)
print(low * high)