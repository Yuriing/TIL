import sys
sys.stdin = open('input2005.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    triangle = []
    for i in range(1, N+1):
        triangle.append([0]*i)

    triangle[0][0] = 1

    for i in range(N):
        for n in range(i+1):
            if i == 0:
                triangle[i][n] = 1
            elif i == 1:
                triangle[i][n] = 1
            elif n == i:
                triangle[i][n] = 1
            elif n == 0:
                triangle[i][n] = 1
            else:
                triangle[i][n] = triangle[i-1][n-1] + triangle[i-1][n]

    print(f'#{tc}')
    for row in triangle:
        print(*row)
