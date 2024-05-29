import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a = lst[0]
    b = lst[1]
    c = lst[2]
    if a==0 & b==0 & c==0:
        break
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")