import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
def dac(a, b, c):
    if b == 1:
        return a%c
    elif b%2==0:
        return (dac(a,b//2,c)**2)%c
    else:
        return  ((dac(a,b//2,c)**2)*a)%c
print(dac(a, b, c))