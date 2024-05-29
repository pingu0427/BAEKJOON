import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = int(input())
qlst = list(map(int, input().split()))

for i in range(M):
    flag = False
    ok, ng = -1, N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if lst[mid] < qlst[i]:
            ok = mid
        elif lst[mid] == qlst[i]:
            flag = True
            break
        else:
            ng = mid
    if flag == True:
        print(1)
    else:
        print(0)