import sys

n , m = map(int, sys.stdin.readline().rstrip().split())
pokemon = {}
number = {}
for i in range(1,n+1):
    po = sys.stdin.readline().strip()
    pokemon[i] = po
    number[po] = i
for i in range(m):
    string = sys.stdin.readline().rstrip()
    if string.isdigit() == True:
        print(pokemon[int(string)])
    else:
        print(number[string])