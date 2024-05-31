import sys

n = int(sys.stdin.readline().rstrip())
a = [0]
a.append(1)
a.append(1)
i = 3
while i <= n:
    a.append(a[i-2]+a[i-1])
    i += 1
print(a[n])