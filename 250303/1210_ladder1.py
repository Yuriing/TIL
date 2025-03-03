import sys
sys.stdin = open('input1210.txt')

for _ in range(1, 11):
    T = int(input())

    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    for j in range(100):
        if matrix[99][j] == 2:
            r, c = 99, j

    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    while r > 0:
        for i in range(3):
            if 0 <= r+dr[i] < 100 and 0 <= c+dc[i] < 100:
                nr = r + dr[i]
                nc = c + dc[i]

                if matrix[nr][nc] == 1:
                    matrix[nr][nc] = 3
                    r = nr
                    c = nc
                    break
                else:
                    continue

    result = c

    print(f'#{T} {result}')