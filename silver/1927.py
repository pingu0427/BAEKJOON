import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input())
for i in range(n):
    x = int(input())
    if x== 0:
        if not heap:
            print(0)
        else:    
            tmp = heapq.heappop(heap)
            print(tmp)
    else:
        heapq.heappush(heap, x)