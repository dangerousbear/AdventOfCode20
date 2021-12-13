lines = [line[:-1] for line in open("12.txt", "r").readlines()]

pos = complex(10,1)
sPos = complex(0)
def moveCardinal(direction, length, p):
    if direction == "E":
        p += length
    elif direction == "W":
        p -= length
    elif direction == "N":
        p += length * 1j
    elif direction == "S":
        p -= length * 1j
    else:
        print("Failed with dir " + direction)
    return p

def turn(direction, degrees):
    if degrees == 180:
        return -1
    amount = 0
    if degrees == 90:
        amount = 1j
    elif degrees == 270:
        amount = -1j
    else:
        assert(False)
    if direction == "R":
        amount *= -1
    
    return amount

for line in lines:
    symbol = line[0]
    L = int(line[1:])
    if symbol == "F":
        sPos += pos * L
    elif symbol == "R" or symbol == "L":
        pos *= turn(symbol, L)
    else:
        pos = moveCardinal(symbol, L, pos)
    print(pos)

print(abs(sPos.real) + abs(sPos.imag))