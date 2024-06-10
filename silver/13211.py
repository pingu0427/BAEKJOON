import sys
input = sys.stdin.readline

N = int(input())
s = set()
for i in range(N):
    s.add(input())
answer = 0
M = int(input())
for i in range(M):
    if input() in s:
        answer += 1
print(answer)