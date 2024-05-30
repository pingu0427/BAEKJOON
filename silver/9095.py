import sys

n = int(sys.stdin.readline().rstrip())
lst = []
lst.insert(0,1)
lst.insert(1,2)
lst.insert(2,4)
lst.insert(3,7)
for i in range(4,11):
    a = lst[i-3]+lst[i-2]+lst[i-1]
    lst.insert(i,a)
for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    print(lst[m-1])