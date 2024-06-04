import sys
input = sys.stdin.readline

n = int(input().rstrip())
DP = []
for i in range(n):
    DP.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            DP[i][j]+=DP[i-1][j]
        elif j==i:
            DP[i][j]+=DP[i-1][j-1]
        else:
            DP[i][j] += max(DP[i - 1][j - 1], DP[i - 1][j])
print(max(DP[n-1]))