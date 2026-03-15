---
date: '2023-12-20T17:23:55-05:00'
draft: false
title: "Advent of Code Day 20 -- Pulse Propagation"
summary: "First, you find the right answer using pencil and paper. Then, you write code to produce that answer. Right? No? Just me?"
categories:
  - "Advent of Code"
tags:
  - "AoC2023"
  - "Circuits"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-20-16.57.44-Create-an-illustration-inspired-by-the-aesthetic-of-a-retro-sci-fi-movie-similar-to-Tron-avoiding-direct-references-or-copyrighted-elements.-Visualiz.png"
cover: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-20-16.57.44-Create-an-illustration-inspired-by-the-aesthetic-of-a-retro-sci-fi-movie-similar-to-Tron-avoiding-direct-references-or-copyrighted-elements.-Visualiz.png"
---

The elves don't have much to do today, as the puzzle wastes no time getting to the meat: it wants you to [build a digital circuit](https://adventofcode.com/2023/day/20), and then run it.

There's a few components you need to use:

- A **button** sends a low pulse to its outputs

- A **broadcaster** takes a pulse from input and sends it to all its outputs

- A **conjunction** saves the last pulses sent by its inputs and when the saved values for all its inputs are high, it sends a low pulse to its outputs.

- A **flip-flop** switches its state when it receives a low pulse and passes that along to its outputs.

Pressing the button sends a pulse to the broadcaster. All components, including the button, send their pulses by using a **FIFO Queue** (first in, first out). Pressing the button fills up the queue and this continues on until the queue is in a settled state, at which point, the button can be pressed again.

The problem description was pretty clear. I was going to need to make a common component class and subclasses for the different behaviors. I needed a queue. And this was *definitely* going to be implementing an [adder](https://en.wikipedia.org/wiki/Adder_(electronics)).

`def read_data():
    with open('puzzle20.dat') as f:
        data = f.read().splitlines()
    
    component_dict = {'button': Button()}
    name_dict = {}

    # First pass, create components
    for line in data:
        ins, outs = line.split(' -> ')
        create_component(ins, name_dict, component_dict)
        
    # Second pass, connect the components
    for line in data:
        ins, outs = line.split(' -> ')
        connect_components(ins, outs, name_dict, component_dict)
    
    # Connect button to broadcaster as a special case
    component_dict['button'].add_output(component_dict['broadcaster'])
    component_dict['broadcaster'].add_input(component_dict['button'])
    
    return component_dict`

Today's was pretty long, so not going to put in all the code, like the component classes. **read_data** first makes all the components. **button** isn't in the puzzle input, so I add it explicitly. First pass creates the components, second pass connects the inputs and outputs. It lastly connects the button and the broadcaster together.

`def push_the_button(component_dict: dict, counts: dict):
    component_dict['button'].pulse_in(None, State.LOW, pulse_list)

    while not pulse_list.empty():
        dest, source, state = pulse_list.get()
        counts[state] += 1
        dest.pulse_in(source, state, pulse_list)`

Signals are sent by adding them to the **pulse_list**, something every component can do. We start things off by sending a low pulse to **button**, which will pass it along to the broadcaster and get the party started. We loop, sending pulses to components, until there are no more. We count the number of high and low pulses, because that is what part 1 wants.

`def part1():
    component_dict = read_data()
    counts = {State.HIGH: 0, State.LOW: 0}

    for _ in range(1000):
        push_the_button(component_dict, counts)

    print ("Part 1:", counts[State.HIGH] * counts[State.LOW])`

Part 1 wants us to press the button a thousand times and determine the product of the high and low pulses that were sent by any component. So this essentially tests to be sure your circuit is working for part 2.

`def part2():
    global button_presses
    component_dict = read_data()
    counts = {State.HIGH: 0, State.LOW: 0}

    # find the conjunction that feeds 'rx'
    feeder = component_dict['rx'].inputs[0]
    feeder.am_feeder = True

    while True:
        button_presses += 1
        push_the_button(component_dict, counts)
        if feeder.all_flipped():
            print ("Part 2:", lcm(*feeder.input_flipped.values()))
            break`

The explanation is going to be longer than the code, I think. There is one component, **rx**, which has no outputs (and is of the bespoke **Output** component subclass). We need to know when it is sent a low pulse. Now I looked at my input data, and saw that a conjunction was the previous component, so **rx** will get a low pulse when all the inputs to the previous component are high.

I looked at the circuits running to see if I could find a counter in there, but I couldn't. I found seven or eight bits that were counting, but then they ran out, so there's a few things going on in the circuit.

I eventually had the bright idea to see if there was any periodicity in the individual inputs to the conjunction, and found that each bit repeated in a cycle starting from the very first button press. And the cycles four all the inputs were mutually prime. So the answer was to figure out these cycles and multiply their lengths together.

This was our second lowest common multiple problem this year -- this time, I was ready for it.

After manually figuring out the cycles and submitting the answer, I went back and wrote code to allow conjunctions to figure out when all their inputs were high so that we would know we had been through the first cycle with all inputs and could now calculate the answer.

That's it!
