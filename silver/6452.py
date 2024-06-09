while True:
    try:
        A = input()
        n = len(A)
        answer : float = 0
        for i in range(2,n):
            num = int(A[i])*(1000**(n-2))//(8**(i-1))
            answer += int(num)
        answer = str(answer)
        print(A,"[8] =","0."+"0"*(3*(n-2)-len(answer))+ answer,"[10]")
    except:
        break