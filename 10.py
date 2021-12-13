vals = sorted([int(x) for x in open("10.txt", "r").readlines()])
vals.append(vals[-1] + 3)
assert(len(vals) == len(set(vals)))
nPaths = [1, 1, 1]
lastVals = [-6, -3, 0]
for v in vals:
    paths = nPaths[2]
    for i in [0, 1]:
        if (v - lastVals[i] <= 3):
            paths += nPaths[i]
    nPaths.pop(0)
    nPaths.append(paths)
    lastVals.pop(0)
    lastVals.append(v)

print(nPaths[-1])
    
