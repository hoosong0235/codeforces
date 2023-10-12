t = int(input())

for _ in range(t):
    cnt = 0
    isTrue = False
    n, m = map(int, input().split())
    x = input()
    s = input()

    while not isTrue and cnt < 8:
        if s in x:
            print(cnt)
            isTrue = True
        cnt += 1
        x = x + x

    if not isTrue:
        print(-1)
