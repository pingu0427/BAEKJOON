import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string != '0':
        length = len(string)
        n = length//2
        flag = True
        for i in range(n):
            if string[i] != string[-(i+1)]:
                flag = False
                break
        if flag == True:
            print("yes")
        else:
            print("no")
    else: 
        break