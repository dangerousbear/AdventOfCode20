count = 0
for line in open("2.txt", "r").readlines():
    tokens = line.split()
    limits = tokens[0].split("-")
    i1 = int(limits[0]) - 1
    i2 = int(limits[1]) - 1
    char = tokens[1][0]
    count += 1 if (tokens[2][i1] == char) != (tokens[2][i2] == char) else 0

print(count)
