from copy import deepcopy
from enum import Enum
from functools import reduce
import operator
import queue

class FlipFlop:
    def __init__(self, outputs):
        self.on = False
        self.outputs = deepcopy(outputs)

class Conjunction:
    def __init__(self, outputs):
        self.rememberHigh = False
        self.inputs = {}
        self.outputs = deepcopy(outputs)

class Pulse(Enum):
    Low = 0
    High = 1

flipflops = {}
conjunctions = {}
broadcastOutputs = []
buttonPressCount = 0
conjunctionsOfInterest = {'xn': -1, 'qn': -1, 'xf': -1, 'zl': -1}

def AllInputsHigh(conjunction) -> bool:
    return False if Pulse.Low in conjunctions[conjunction].inputs.values() else True

def SendPulse(source, target, pulse, q):
    if source in conjunctionsOfInterest and target == 'th' and pulse == Pulse.High and conjunctionsOfInterest[source] == -1:
        conjunctionsOfInterest[source] = buttonPressCount
    if target in flipflops:
        if pulse == Pulse.Low:
            flipflops[target].on = not flipflops[target].on
            newPulse = Pulse.High if flipflops[target].on else Pulse.Low
            q.put((target, newPulse))
    elif target in conjunctions:
        conjunctions[target].inputs[source] = pulse
        newPulse = Pulse.Low if AllInputsHigh(target) else Pulse.High
        q.put((target, newPulse))

def PushButton():
    q = queue.Queue()
    for flipflop in broadcastOutputs:
        SendPulse("broadcaster", flipflop, Pulse.Low, q)
    while not q.empty():
        module, pulse = q.get()
        if module in flipflops:
            for output in flipflops[module].outputs:
                SendPulse(module, output, pulse, q)
        else:
            for output in conjunctions[module].outputs:
                SendPulse(module, output, pulse, q)

# Main
file = open('sample_input.txt', 'r')
content = file.read()
for line in content.splitlines():
    splitted = line.replace(',', '').split(' ')
    name = splitted[0][1:] if not splitted[0][0].isalpha() else splitted[0]
    if line[0] == '%':
        flipflops[name] = FlipFlop(deepcopy(splitted[2:]))
    elif line[0] == '&':
        conjunctions[name] = Conjunction(deepcopy(splitted[2:]))
    else:
        broadcastOutputs = deepcopy(splitted[2:])

for line in content.splitlines():
    splitted = line.replace(',', '').split(' ')
    if splitted[0] == 'broadcaster':
        continue
    input = splitted[0][1:]
    for output in splitted[2:]:
        if output in conjunctions:
            conjunctions[output].inputs[input] = Pulse.Low


while -1 in conjunctionsOfInterest.values():
    buttonPressCount += 1
    PushButton()

print(reduce(operator.mul, conjunctionsOfInterest.values(), 1))