import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

n,m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
count = 0
for i in range(1,n+1):
    if visited[i] == False:
        count += 1
        dfs(i)
print(count)
            