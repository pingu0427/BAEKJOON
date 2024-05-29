import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
lst = deque()
for i in range(n):
    word = sys.stdin.readline().rstrip().split()
    if word[0] == "push_back":
        lst.append(int(word[1]))
    if word[0] == "push_front":
        lst.appendleft(int(word[1]))
    elif word[0] == "pop_front":
        if lst:
            a = lst.popleft()
            print(int(a))
        else:
            print(-1)
    elif word[0] == "pop_back":
        if lst:
            a = lst.pop()
            print(int(a))
        else:
            print(-1)
    elif word[0] == "back":
        if lst:
            print(lst[-1])
        else:
            print(-1)
    elif word[0] == "front":
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif word[0] == "size":
        print(len(lst))
    elif word[0] == "empty":
        if lst:
            print(0)
        else:
            print(1)