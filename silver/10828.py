import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    word = sys.stdin.readline().rstrip().split()
    if word[0] == "push":
        lst.append(int(word[1]))
    elif word[0] == "pop":
        if lst:
            a = lst.pop()
            print(int(a))
        else:
            print(-1)
    elif word[0] == "top":
        if lst:
            print(lst[-1])
        else:
            print(-1)
    elif word[0] == "size":
        print(len(lst))
    elif word[0] == "empty":
        if lst:
            print(0)
        else:
            print(1)