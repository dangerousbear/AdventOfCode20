lines = [line[:-1] for line in open("14.txt", "r").readlines()]
masks = []
writesPerMask = []
for line in lines:
    tokens = line.split(" = ")
    lh = tokens[0]
    if lh == "mask":
        masks.append(tokens[1])
        writesPerMask.append([])
    else:
        loc = int(lh[lh.index("[")+1:lh.index("]")])
        writesPerMask[-1].append((loc, int(tokens[1])))
        

writtenVals = dict()

for i, mask in enumerate(masks):
    writes = writesPerMask[i]
    
    for loc, intVal in writes:
        binStr = f"{loc:#038b}"[2:]
        assert(len(binStr) == len(mask))
        s = ""
        for n in range(len(binStr)):
            s += binStr[n] if mask[n] == "0" else mask[n]
        numX = s.count("X")
        for n in range(2 ** numX):
            nBinStr = f"{n:#0b}"[2:]
            nBinStr = (numX - len(nBinStr)) * "0" + nBinStr
            binStrIdx = 0
            s2 = ""
            for si in range(len(s)):
                if (s[si] != "X"):
                    s2 += s[si]
                else:
                    s2 += nBinStr[binStrIdx] if binStrIdx < len(nBinStr) else "0"
                    binStrIdx += 1
            assert(binStrIdx == numX)
            newLoc = int(s2,2)
            writtenVals[newLoc] = intVal

count = 0         
for v in writtenVals:
    count += writtenVals[v]
print(count)
    


# writesPerMask = []
# for line in lines:
#     tokens = line.split(" = ")
#     lh = tokens[0]
#     if lh == "mask":
#         masks.append(tokens[1])
#         writesPerMask.append([])
#     else:
#         loc = int(lh[lh.index("[")+1:lh.index("]")])
#         writesPerMask[-1].append((loc, int(tokens[1])))
        

# writtenVals = dict()

# for i, mask in enumerate(masks):
#     writes = writesPerMask[i]
    
#     for loc, intVal in writes:
#         binStr = f"{intVal:#038b}"[2:]
#         assert(len(binStr) == len(mask))
#         s = ""
#         for n in range(len(binStr)):
#             s += binStr[n] if mask[n] == "X" else mask[n]
#         print("writing " + s)
#         writtenVals[loc] = int(s,2)

# count = 0         
# for v in writtenVals:
#     count += writtenVals[v]
# print(count)