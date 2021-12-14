vals = [int(x) for x in open("15.txt", "r").readlines()[0][:-1].split(",")]
N = 30000000

lastPos = dict()

for i in range(len(vals)):
    lastPos[vals[i]] = i

last = vals[-1]
for i in range(len(vals), N):
    newLast = 0 if last not in lastPos else i - 1 - lastPos[last]
    lastPos[last] = i - 1
    last = newLast
print(last)
