from copy import deepcopy
from enum import Enum
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
pulseCount = [0, 0]

def AllInputsHigh(conjunction) -> bool:
    return False if Pulse.Low in conjunctions[conjunction].inputs.values() else True

def SendPulse(source, target, pulse, q):
    if target in flipflops:
        if pulse == Pulse.Low:
            flipflops[target].on = not flipflops[target].on
            newPulse = Pulse.High if flipflops[target].on else Pulse.Low
            q.put((target, newPulse))
    elif target in conjunctions:
        conjunctions[target].inputs[source] = pulse
        newPulse = Pulse.Low if AllInputsHigh(target) else Pulse.High
        q.put((target, newPulse))
    pulseCount[pulse.value] += 1

def PushButton():
    q = queue.Queue()
    pulseCount[Pulse.Low.value] += 1
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

for _ in range(1000):
    PushButton()

print(pulseCount[Pulse.Low.value] * pulseCount[Pulse.High.value])