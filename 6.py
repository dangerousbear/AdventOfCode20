lines = [line[:-1] for line in open("6.txt", "r").readlines()]

chars = dict()
count = 0
nPeople = 0
for line in lines:
    if (line == ''): #New group
        for c in chars:
            if chars[c] == nPeople:
                count += 1
        chars = dict()
        nPeople = -1
    nPeople += 1
    for c in line:
        chars[c] = chars[c] + 1 if c in chars else 1
print(count)