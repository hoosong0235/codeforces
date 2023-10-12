def f(n, v, es, marked):
    reached = [False for _ in range(n + 1)]
    reached[v] = True
    cnt = 0

    if all(reached[m] for m in marked):
        return cnt

    while True:
        cnt += 1
        reach = list()

        for i in range(len(reached)):
            if reached[i]:
                for e in es:
                    if e[0] == i:
                        reach.append(e[1])
        
        for r in reach:
            reached[r] = True

        if all(reached[m] for m in marked):
            return cnt


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    marked = list(map(int, input().split()))

    vs = [i + 1 for i in range(n)]
    es = list()
    for _ in range(n - 1):
        u, v = map(int, input().split())
        es.append((u, v))
        es.append((v, u))
    
    lst = [f(n, v, es, marked) for v in vs]
    # print(lst)
    print(min(lst))