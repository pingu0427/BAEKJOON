import sys

n = int(sys.stdin.readline().rstrip())
a = 0
i = 0
while a < n:
    i += 1
    if '666' in str(i):
        a += 1
print(i)