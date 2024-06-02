import sys
N, r, c = map(int, sys.stdin.readline().split())

visit = 0
while N != 0:
    N -= 1
    size = 2**N
    if r < size and c < size:
        visit += 0
    elif r<size and c >= size:
        visit += size*size
        c -= size
    elif r>=size and c< size:
        visit += 2*size*size
        r -= size
    else:
        visit += 3*size*size
        r -= size
        c -= size
print(visit)