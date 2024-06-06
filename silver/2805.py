import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def cut(x, h):
    if x <= h:
        return 0
    else:
        return x-h
start, end = 1, sum(trees)
while start <= end:
    count = 0
    mid = (start+end)//2
    for i in range(n):
        count += cut(trees[i], mid)
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)