import sys
input = sys.stdin.readline

n = int(input())
def test(stringing):
    lst = []
    string = stringing
    flag = True
    for i in range(len(string)):
        if string[i] == '(':
            lst.append('o')
        elif string[i] == ')':
            if not lst:
                flag = False
                break
            else:    
                lst.pop()
    if lst:
        flag = False
    if flag == True:
        print("YES")
    else:
        print("NO")
for i in range(n):
    test(input())