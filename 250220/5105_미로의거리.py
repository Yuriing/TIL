import sys
sys.stdin = open('input5105.txt')


def find_way(i, j, N):  # 시작위치[i][j], 크기 N
    visited = [[0]*N for _ in range(N)]  # visited 생성
    # 방문 여부를 이차원 배열에 저장

    q = []  # 큐 생성
    q.append([i, j])  # 시작점 인큐
    visited[i][j] = 1  # 시작점 인큐 표시

    while q:  # 큐에 남은 칸이 없을 때까지
        ti, tj = q.pop(0)

        if maze_matrix[ti][tj] == 3:  # 출구 확인. 출구에 도착하면 1 아니면 0
            return 1

        # t에 인접한 정점 w 중 인큐되지 않은 곳이면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            # 미로를 벗어나지 않고 벽이 아니고
            if 0 <= wi < N and 0 <= wj < N and maze_matrix[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1


def find_start(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    maze_matrix = []
    for _ in range(N):
        maze_matrix.append(list(map(int, input().strip())))

    sti, stj = find_start(N, maze_matrix)

    ans = find_way(sti, stj, N)
    print(ans)
