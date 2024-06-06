import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n >= m/2:
    print('E')
else:
    print('H')