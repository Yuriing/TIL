# 01 BFS 예제
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''


def BFS(s, V):  # 시작점, 마지막 정점
    # visited 생성
    visited = [0] * (V+1)

    # 큐 생성
    q = []  # 시작점 넣어놓고 시작
    q.append(s)

    # 시작점 인큐 표시
    visited[s] = 1

    # 큐가 비워질 때까지 반복
    while q:
        # 디큐해서 t에 저장
        t = q.pop(0)
        print(t, end='')
        # t 정점에 관련한 처리
        # t에 인접한 정점 w 중 인큐되지 않은 정점이 있으면
        for w in adj_l[t]:
            if visited[w] == 0:  # 인큐, 인큐 표시
                q.append(w)
                visited[w] = visited[t] + 1
        

v, e = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트 ----------------------------
adj_l = [[] for _ in range(v+1)]
for i in range(e):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
# --------------------------------------
BFS(1, 7)


# 02 미로탐색
def BFS2(i, j, N):  # 시작위치[i][j], 크기 N
    visited = [[0]*N for _ in range(N)]  # visited 생성
    q = []  # 큐 생성
    q.append([i, j])  # 시작점 인큐
    visited[i][j] = 1  # 시작점 인큐 표시

    while q:  # 큐에 남은 칸이 없을 때까지(큐가 다 비워질 때까지)
        ti, tj = q.pop(0)  # 디큐해서 t에 넣어주고
        if maze[ti][tj] == '3':  # 출구 확인. 출구에 도착하면 1 아니면 0
            return 1

        # t에 인접한 정점 w 중 인큐되지 않은 곳이면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            # 미로를 벗어나지 않고 벽이 아니고
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                q.append([wi, wj])  # 인큐 후 표시
                visited[wi][wj] = visited[ti][tj] + 1


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


N = int(input())  # 미로의 가로 크기
maze = [input() for _ in range(N)]

sti, stj = find_start(N)

ans = BFS2(sti, stj)
print(ans)