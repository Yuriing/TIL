import sys
sys.stdin = open('input1953.txt')

types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    visited = [row[:] for row in matrix]

    q = []
    visited[R][C] = 11
    q.append((R, C))

    while q:
        r, c = q.pop(0)
        current = matrix[r][c]

        for i in range(4):
            if types[current][i] == 0:
                continue

            if 0 <= r+dr[i] < N and 0 <= c+dc[i] < M:  # 새 좌표가 벽 안쪽에 있을 때
                nr = r + dr[i]
                nc = c + dc[i]

                if matrix[nr][nc] > 0:  # 통로가 놓인 곳일 때
                    # 상-하 혹은 좌-우 가 둘 다 1이라면(두 지점이 연결되어있다면)
                    if (types[matrix[nr][nc]][0] == types[current][1] == 1 or
                            types[matrix[nr][nc]][2] == types[current][3] == 1 or
                            types[current][0] == types[matrix[nr][nc]][1] == 1 or
                            types[current][2] == types[matrix[nr][nc]][3] == 1):

                        if visited[nr][nc] < 11:  # 방문하지 않은 곳일 때
                            q.append((nr, nc))
                            visited[nr][nc] = visited[r][c] + 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 10 < visited[i][j] <= 10+L:  # visited 처리한 곳 개수 세기
                cnt += 1

    print(f'#{tc} {cnt}')


