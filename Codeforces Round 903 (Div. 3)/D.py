import sys


t = int(sys.stdin.readline())

for _ in range(t):
    isTrue = True
    n = int(sys.stdin.readline())

    a = map(int, sys.stdin.readline().split())
    mul = 1
    for i in a:
        mul *= i

    d = 2
    cnt = 0
    while d <= mul:
        if mul % d == 0:
            cnt += 1
            mul = mul // d
        else:
            if cnt % n != 0:
                isTrue = False
                break
            cnt = 0
            d = d + 1
    
    if cnt % n != 0:
        isTrue = False
    
    if isTrue:
        print("YES")
    else:
        print("NO")