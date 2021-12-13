import copy
vals = [[int(x) for x in line[:-1].replace("#", "2").replace("L", "1").replace(".","0")] for line in open("11.txt", "r").readlines()]
Ly = len(vals)
Lx = len(vals[0])

def neighbors(i0, j0, vals):
    nbors = []
    i, j = i0, j0
    while i > 0:
        i -= 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
            
    i, j = i0, j0
    
    while i + 1 < Ly:
        i += 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
        
    
    i, j = i0, j0
    while j > 0:
        j -= 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
        
            
    i, j = i0, j0
    while j + 1 < Lx:
        j += 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
        
        
    i, j = i0, j0
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
        
            
    i, j = i0, j0
    while i + 1 < Ly and j + 1 < Lx:
        i += 1
        j += 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
        

    i, j = i0, j0
    while i > 0 and j + 1 < Lx:
        i -= 1
        j += 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
        
            
    i, j = i0, j0
    while i + 1 < Ly and j > 0:
        i += 1
        j -= 1
        if vals[i][j] > 0:
            nbors.append((i,j))
            break
        
    
    return nbors


def evolve(vals):
    new = copy.deepcopy(vals)
    for i in range(Ly):
        for j in range(Lx):
            v = vals[i][j]
            if ( v == 0 ):
                new[i][j] = 0
            elif ( v == 1 ):
                new[i][j] = 2 if all(vals[i2][j2] < 2 for i2,j2 in neighbors(i,j, vals)) else 1
            else:
                new[i][j] = 1 if sum(vals[i2][j2]  == 2 for i2,j2 in neighbors(i,j, vals)) >= 5  else 2
    return new


n = 0
while True:
    # print(vals)
    new = evolve(vals)
    if (new == vals):
        break
    vals = new
    n += 1

count = 0
for i in range(Ly):
    for j in range(Lx):
        if vals[i][j] == 2:
            count += 1
print(count)