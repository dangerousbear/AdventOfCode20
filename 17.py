import numpy as np

N = 6
vals = [[int(x) for x in line[:-1].replace(".","0").replace("#","1")] for line in open("17.txt", "r").readlines()]

x = np.zeros((2*N+1, len(vals) + 2*N, len(vals[0]) + 2*N, 2*N+1), dtype=int)
for i, row in enumerate(vals):
    for j, v in enumerate(row):
        x[N][N+i][N+j][N] = v
    
xs, ys, zs, ws = x.shape

def neighbors(i,j,k, l):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            for dk in range(-1, 2):
                for dl in range(-1, 2):
                    if not (di == 0 and dj == 0 and dk == 0 and dl == 0):
                        yield (i + di, j + dj, k + dk, l + dl)

for step in range(N):
    print(sum(sum(sum(sum(x == 1)))))
    xNew = x.copy()
    for i in range(xs):
        for j in range(ys):
            for k in range(zs):
                for l in range(ws):
                    nCount = 0
                    for (ni, nj, nk, nl) in neighbors(i,j,k,l):
                        try:
                            nCount += x[ni, nj, nk, nl]
                        except:
                            pass
                    xNew[i,j,k,l] = (2 <= nCount and nCount <= 3) if x[i,j,k,l] == 1 else nCount == 3
    x = xNew

print(sum(sum(sum(sum(x == 1))))) 
# def getNext(v):
#     print(new)
    