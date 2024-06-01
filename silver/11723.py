import sys

n = int(sys.stdin.readline().rstrip())
s = set()
for i in range(n):
    string = sys.stdin.readline().rstrip().split()
    if len(string) > 1:
        command, target = string[0], string[1]
        target = int(target)
        if command == 'add':
            s.add(target)
        if command == 'remove':
            s.discard(target)
        if command == 'check':
            print(1 if target in s else 0)
        if command == 'toggle':
            if target in s:
                s.discard(target)
            else:
                s.add(target)
    else:
        command = string[0]
        if command == 'all':
            s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        if command == 'empty':
            s = set()