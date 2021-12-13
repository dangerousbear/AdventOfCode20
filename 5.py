lines = [line[:-1].replace("F","0").replace("B","1").replace("L","0").replace("R","1") for line in open("5.txt", "r").readlines()]

ids = []
for line in lines:
    row = int(line[:7],2)
    col = int(line[7:],2)
    ids.append(row*8 + col)

ids = sorted(ids)
print([x for x in ids if x+2 in ids and x+1 not in ids][0] + 1)