t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    m = min(a, b, c)

    if not (a % m == 0 and b % m == 0 and c % m == 0):
        print("NO")
        continue

    if (a // m + b // m + c // m) <= 6:
        print("YES")
    else:
        print("NO")
