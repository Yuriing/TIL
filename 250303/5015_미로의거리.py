import sys
import copy
sys.stdin = open('input5105.txt')

def findtheway(N, adj_matrix):
    adj_visited = copy.deepcopy(adj_matrix)
    q = []

    for i in range(N):
        for j in range(N):
            if adj_matrix[i][j] == 2:
                adj_visited[i][j] = 5
                r, c = i, j

    q.append((r, c))

    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]

    while q:
        r, c = q.pop(0)
        current_place = adj_matrix[r][c]

        for i in range(4):
            if 0 <= r+dr[i] < N and 0 <= c+dc[i] < N:
                nr = r + dr[i]
                nc = c + dc[i]

                if adj_matrix[nr][nc] == 0 and adj_visited[nr][nc] == 0:
                    q.append((nr, nc))
                    adj_visited[nr][nc] = adj_visited[r][c] + 1

                elif adj_matrix[nr][nc] == 3:
                    return adj_visited[r][c] - 5
                
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    adj_matrix = []
    for _ in range(N):
        adj_matrix.append(list(map(int, input().strip())))

    result = findtheway(N, adj_matrix)

    print(f'#{tc} {result}')