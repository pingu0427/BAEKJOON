import sys
input = sys.stdin.readline

n = int(input())
price = []
DP = [[0]*3 for _ in range(n)]
for i in range(n):
    price.append(list(map(int, input().split())))
DP[0] = price[0]
for j in range(n):
    DP[j][0] = min(DP[j-1][1],DP[j-1][2])+ price[j][0]
    DP[j][1] = min(DP[j-1][0],DP[j-1][2])+ price[j][1]
    DP[j][2] = min(DP[j-1][0],DP[j-1][1])+ price[j][2]

print(min(DP[n-1]))