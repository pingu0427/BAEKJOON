import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    f = int(sys.stdin.readline().rstrip())
    DP = [[]]*41
    DP[0] = [1,0]
    DP[1] = [0,1]
    DP[2] = [1,1]

    for j in range(3,1+f):
        DP[j] = [DP[j-1][0]+DP[j-2][0],DP[j-1][1]+DP[j-2][1]]
    print(DP[f][0],DP[f][1])
