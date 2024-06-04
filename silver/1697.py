import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
visited = [0]*100001
def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break
        for j in (x-1,x+1,x*2):
            if 0 <= j < 100001 and not visited[j]:
                visited[j] = visited[x] + 1
                queue.append(j)
bfs()