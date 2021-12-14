lines = [line.replace(" ", "") for line in open("18.txt", "r").readlines()]
import operator as op

operators = {"*":op.mul,"+":op.add}

def evaluate(data):
    total = 0
    operate = None
    char=next(data,")")
    while char!=")" and char!="\n":
        if char in operators:
            operate = operators[char]
            if char == "*":
                return operate(total,evaluate(data))
            char=next(data,")")
            continue
        value = evaluate(data) if char == "(" else int(char)
        total = value if operate is None else operate(total,value)
        char=next(data,")")
    return total

totSum = 0
for line in lines:
    totSum += evaluate(iter(line))
print(totSum)