t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    matrix = []

    for _ in range(n):
        matrix.append(input())

    for i in range(n):
        for j in range(n):
            a, b, c, d = matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i]
            if a != b or a != c or a != d or b != c or b != d or c != d:
                mx = max(ord(a), ord(b), ord(c), ord(d))

                for char in [a, b, c, d]:
                    cnt += mx - ord(char)

                matrix[i] = matrix[i][:j] + chr(mx) + matrix[i][j+1:]
                matrix[j] = matrix[j][:n-i-1] + chr(mx) + matrix[j][n-i:]
                matrix[n-i-1] = matrix[n-i-1][:n-j-1] + chr(mx) + matrix[n-i-1][n-j:]
                matrix[n-j-1] = matrix[n-j-1][:i] + chr(mx) + matrix[n-j-1][i+1:]
            
    print(cnt)
