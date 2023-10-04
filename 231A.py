n = int(input())
num = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        num += 1
print(num)
