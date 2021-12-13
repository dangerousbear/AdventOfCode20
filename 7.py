lines = [line[:-1] for line in open("7.txt", "r").readlines()]

contains = dict()

for line in lines:
    sides = line.split(" contain ")
    lh, rh = sides[0], sides[1][:-1]
    lBagName = lh.split()[0] + lh.split()[1]
    rhTokens = rh.split(", ")
    for nBags in rhTokens:
        toks = nBags.split()
        if (len(toks) == 3):
            pass
        elif (len(toks) == 4):
            rBagName = toks[1] + toks[2]
            if lBagName not in contains:
                contains[lBagName] = set()
            contains[lBagName].add((rBagName, int(toks[0])))
            pass
        else:
            assert(False)

def search(bag):
    count = 1
    if bag in contains:
        for b, c in contains[bag]:
            print(bag + " -> " + b + " count " + str(c))
            count += c * search(b)
    return count

print(search("shinygold") - 1)