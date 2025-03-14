import sys
sys.stdin = open('input1861.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    visited = [0] * (N*N + 1)

    r = 0
    c = 0
    for r in range(N):
        for c in range(N):
            for i in range(4):
                if 0 <= r + dr[i] < N and 0 <= c +dc[i] < N:
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if matrix[nr][nc] == matrix[r][c] + 1:
                        visited[matrix[r][c]] = 1
                        break

    count = 0
    mx_cnt = 0
    start = 0
    for i in range(N*N, -1, -1):
        if visited[i] == 1:
            count += 1
        else:
            if mx_cnt <= count:
                mx_cnt = count
                start = i + 1
            count = 0

    print(f'#{tc} {start} {mx_cnt + 1}')
