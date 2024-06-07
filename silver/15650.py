import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

numList = [i for i in range(1, N+1)]

for ss in combinations(numList, M):
    print(*ss)