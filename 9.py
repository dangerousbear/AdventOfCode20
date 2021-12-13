vals = [int(x) for x in open("9.txt", "r").readlines()]

invalidNum = 393911906

for start in range(0, len(vals)):
    s = vals[start]
    for stop in range(start+1, len(vals)):
        s += vals[stop]
        if (s == invalidNum):
            print("Found it, start stop " + str(start) + " " + str(stop))
            r = [vals[i] for i in range(start, stop+1)]
            print(min(r) + max(r))
        if (s > invalidNum):
            break
