import sys
input = sys.stdin.readline

n = int(input())
point = [0]*(n+1)
for i in range(1,n+1):
    point[i] = int(input())

dp = [0]*(n+1)
dp[1] = point[1]
if n >1:
    dp[2] = point[1] + point[2]
if n >2:
    dp[3] = max(point[1]+point[3],point[2]+point[3])
if n >3:
    for i in range(4,n+1):
        dp[i] = max(dp[i-3]+point[i-1]+point[i],dp[i-2]+point[i])
print(dp[n])