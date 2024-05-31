import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
d = list(map(int, sys.stdin.readline().rstrip().split()))

a= 0
answer = 0
for i in range(n):
    a += d.pop(d.index(min(d)))
    answer += a
print(answer)