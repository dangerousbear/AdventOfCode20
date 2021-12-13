from functools import reduce
def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

lines = [line[:-1] for line in open("13.txt", "r").readlines()]
ids = [int(x) for x in lines[1].replace("x","-1").split(",")]
realIDs = [i for i in ids if i >= 0]
remainders = [i - ids.index(i) for i in realIDs]
print(chinese_remainder(realIDs, remainders))


for t in range(0, max(ids)):
    if all(t % i == i for i in ids if i != -1):
        print(t)
        assert(False)