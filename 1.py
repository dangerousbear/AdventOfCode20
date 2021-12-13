vals = [int(line) for line in open("1.txt", "r").readlines()]
for v1 in vals:
    for v2 in vals:
        for v3 in vals:
            if (v1 + v2 + v3 == 2020):
                print(v1)
                print(v2)
                print(v3)