import sys

lst = [(0,1,2,3),(0,1,4,5),(4,5,6,7),(2,3,6,7),(1,3,5,7),(0,2,4,6)]
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    pro_lst = list(map(int,sys.stdin.readline().rstrip().split()))
    pro_lst.sort()
    pro_lst = tuple(pro_lst)
    if pro_lst in lst:
        print("YES")
    else:
        print("NO")