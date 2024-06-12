T = int(input())
    
def factorial_for(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

for i in range(T):
    N, M = map(int, input().split())
    answer = factorial_for(M)//(factorial_for(M-N)*factorial_for(N))
    print(answer)