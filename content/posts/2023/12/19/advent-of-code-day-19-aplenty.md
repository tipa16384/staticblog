---
date: '2023-12-19T21:09:24-05:00'
draft: false
title: "Advent of Code Day 19 -- Aplenty"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2023/12/19/advent-of-code-day-19-aplenty/"
disableHLJS: false
disableShare: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
summary: "First puzzle in a few days where I didn't need to get hints. I guess the problem was musical, aerodynamic, shiny AND extremely cool looking!"
description: "First puzzle in a few days where I didn't need to get hints. I guess the problem was musical, aerodynamic, shiny AND extremely cool looking!"
tags:
  - "Advent of Code"
  - "AoC2023"
  - "Elf"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-19-20.12.32-A-whimsical-and-detailed-illustration-set-on-Gear-Island-where-a-magical-workshop-is-bustling-with-activity.-Elves-dressed-in-colorful-attire-are-b.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-19-20.12.32-A-whimsical-and-detailed-illustration-set-on-Gear-Island-where-a-magical-workshop-is-bustling-with-activity.-Elves-dressed-in-colorful-attire-are-b.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

Yeah, pretty pumped. I did this puzzle in my own head. Part 1 I did, I thought, in a sneaky way, and I was hoping it would be sneaky enough for Part 2. Nope, Part 2 shook up the parts box, but I thought of an approach in the morning, and when I sat down to implement it after dinner, it took a little work, but I got the correct solution for both the sample puzzle input and the real puzzle input, first time.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/12/image-18-258x300.png" class="align-left" >}}

So, thanks to your efforts on the Gear Island, things here on Desert Island are busy as anything. The elves are just tossing parts down from the island above, and [the elves here are a little bit overwhelmed](https://adventofcode.com/2023/day/19). In part 1, the elves want you to determine whether parts are accepted or rejected based on a list of rules.

The sample data is on the left. The parts are described by 'x', 'm', 'a' and 's' properties (e**x**tremely cool looking, **m**usical, **a**erodynamic and **s**hiny), and rules (starting with rule **in**), determine how to process the part until it reaches rules **A** or **R** which mark the part accepted or rejected.

So I've used **lambda** in the past -- these are Python's anonymous functions. For part 1, I processed the rules into lambdas that are put into a dictionary indexed by rule name, and then I simply ran it for each part.

`rule_dict = { 'A': lambda _: True, 'R': lambda _: False }

def process_rule(rule_code):
    m = re.match(r'^(\w+)\{(.*)\}', rule_code)
    rule_name = m.group(1)
    rule = 'lambda part: '
    for instr in m.group(2).split(','):
        if ':' not in instr:
            rule += "rule_dict['{}'](part)".format(instr)
        else:
            cond, cons = instr.split(':')
            prop, comp, val = cond[0], cond[1], int(cond[2:])
            rule += "rule_dict['{}'](part) if part['{}'] {} {} else ".format(cons, prop, comp, val)
    rule_dict[rule_name] = eval(rule)

def part1():
    with open('puzzle19.dat') as f:
        # split on blank line
        data = f.read().split('\n\n')
    
    for rule in data[0].splitlines():
        process_rule(rule)

    parts = [{p1.split('=')[0]: int(p1.split('=')[1]) \
        for p1 in part[1:-1].split(',')} for part in data[1].splitlines()]

    part1 = sum([sum(part.values()) for part in parts if rule_dict['in'](part)])
    print ("Part 1:",part1)`

I don't think anyone actually reads this code. I sure don't. Just want to point out whenever you see the **eval** function in Python code, someone is using code to write more code, making debugging more or less impossible. The dictionary **rule_dict** has the starter rules for **A** and **R**.

**Part 2**

Part 2 doesn't use the list of parts at all. It asks you to solve the list of rules to find out which values of X, M, A and S will lead to accepted parts once all the rules are run. 

So the rules have three patterns: The first is just a rule name -- proceed directly to that rule 100% of the time. The other two is, a part property is less than some value, or a part property is greater than some property. I pass the minimum and maximum values for X, M, A and S through this process as a dictionary of tuples, where the tuples are all initially (1, 4000), the minimum and maximum values. The idea is to keep narrowing this range until we have the final valid range(s).

So there are three outcomes for each rule with a condition:

- Both minimum and maximum satisfy the condition. Just pass the range to the next rule unmodified.

- Both minimum and maximum do not satisfy the condition. Ignore this rule and go to the next.

- The value is between the minimum and the maximum.

The last one is the most fun. You split the range into two ranges, and send the range that satisfies the rule to the rule given, and send the range that does not, to the next rule in the list.

`def lets_go_helper(part, rules, rule):
    rv = 0

    for step in rules[rule]:
        if ':' not in step:
            rv += lets_go(part, rules, step)
            continue
        condition, next_rule = step.split(':')
        x = condition[0]
        xv = part[x]
        lgt = condition[1]
        val = int(condition[2:])

        # Determine if the rule applies 100%
        if (lgt == '' and xv[0] > val and xv[1] > val):
            rv += lets_go(part, rules, next_rule)
            break

        # Check if the rule doesn't apply at all
        if (lgt == '= val and xv[1] >= val) or \
        (lgt == '>' and xv[0] '
            modified_part[x] = (val + 1, xv[1])
            part[x] = (xv[0], val)

        rv += lets_go(modified_part, rules, next_rule)
    return rv

def lets_go(part, rules, rule):
    match rule:
        case 'A':
            return (part['x'][1]-part['x'][0]+1) * (part['m'][1]-part['m'][0]+1) * \
                (part['a'][1]-part['a'][0]+1) * (part['s'][1]-part['s'][0]+1)
        case 'R':
            return 0
        case _:
            return lets_go_helper(part, rules, rule)
        
def part2():
    with open('puzzle19.dat') as f:
        # split on blank line
        data = f.read().split('\n\n')
    
    xmas = {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}
    p2rules = {rule[:rule.index('{')] : rule[rule.index('{')+1:-1].split(',') for rule in data[0].splitlines()}
    print ("Part 2:", lets_go(xmas, p2rules, 'in'))`

I was going to make this into a bunch of lambda, too, but that didn't seem like it would save any time or anything.

Into the home stretch, now!
