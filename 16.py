lines = [line[:-1] for line in open("16.txt", "r").readlines()]
def addToDict(k, v, d):
    d[k] = d[k] + v if k in d else v
newLinesFound = 0

tag2ranges = dict()
myTicket = []
nearbyTickets = []

for line in lines:
    if line == "":
        newLinesFound += 1
        continue
    toks = line.split(": ")
    if newLinesFound == 0:
        tag2ranges[toks[0]] = []
        ranges = toks[1].split(" or ")
        for r in ranges:
            vals = r.split("-")
            tag2ranges[toks[0]].append((int(vals[0]), int(vals[1])))
    elif newLinesFound == 1:
        if "," in line:
            myTicket = [int(x) for x in line.split(",")]
    elif newLinesFound == 2:
        if "," in line:
            nearbyTickets.append([int(x) for x in line.split(",")])
        
def between(l, x, u):
    return l <= x and x <= u

goodTickets = []
for t in nearbyTickets:
    if all(any(any(between(l, v, u) for l,u in tag2ranges[tag]) for tag in tag2ranges) for v in t):
        goodTickets.append(t)

valsPerPos = []
for i in range(len(goodTickets[0])):
    valsPerPos.append(set())
for t in goodTickets:
    for vIdx, v in enumerate(t):
        valsPerPos[vIdx].add(v)
        
tagOrder = [""] * len(tag2ranges)
remainingTags = set(tag2ranges.keys())
while len(remainingTags) > 0:
    for i, vals in enumerate(valsPerPos):
        okTags = remainingTags.copy()
        for v in vals:
            okTagsForVal = set()
            for tag in tag2ranges:
                for l,u in tag2ranges[tag]:
                    if between(l, v, u): 
                        okTagsForVal.add(tag)
            okTags.intersection_update(okTagsForVal)
        if len(okTags) == 1:
            tagOrder[i] = next(iter(okTags))
            remainingTags.remove(next(iter(okTags)))
        
prod = 1
for i, v in enumerate(myTicket):
    if "departure" in tagOrder[i]:
        prod *= v

print(prod)
    

    