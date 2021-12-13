lines = open("8.txt", "r").readlines()

for skipIdx in range(636):
    i = 0
    visitedIndices = []
    acc = 0
    passedSkip = False
    while True:
        if (i + 1 >= len(lines)):
            print("reached end, skipIdx = " + str(skipIdx) + " acc " + str(acc))
            break
        passedSkip = passedSkip or i == skipIdx
        # if (passedSkip):
            # print("Post skip " + str(i))
        toks = lines[i].split()
        if i in visitedIndices:
            # print("Breaking at i = " + str(i))
            break
        visitedIndices.append(i)
        if toks[0] == "nop":
            i += 1
        if toks[0] == "acc":
            acc += int(toks[1])
            i += 1
        if toks[0] == "jmp":        
            i += int(toks[1]) if i != skipIdx else 1

# for i, line in enumerate(lines):
#     toks = lines[i].split()
#     if toks[0] == "jmp":
#         if i + int(toks[1]) > 628:
#             print(i)
# print(acc)