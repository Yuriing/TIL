import sys
sys.stdin = open('input4875.txt')
import copy

def mazerun(N, adj_matrix):
    adj_visited = copy.deepcopy(adj_matrix)
    adj_stack = []

    # 상, 좌, 우, 하
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]

    for i in range(N):
        for j in range(N):
            if adj_matrix[i][j] == 2:
                r, c = i, j
    
    adj_stack.append((r, c))

    while adj_stack:
        r, c = adj_stack.pop()
        current_place = adj_matrix[r][c]

        if adj_visited[r][c] == 0 or adj_visited[r][c] == 2:
            adj_visited[r][c] = 4

        for i in range(4):
            if 0 <= r+dr[i] < N and 0 <= c+dc[i] < N:
                nr = r + dr[i]
                nc = c + dc[i]

                if adj_matrix[nr][nc] == 0 and adj_visited[nr][nc] == 0:
                    adj_stack.append((nr, nc))
                elif adj_matrix[nr][nc] == 3:
                    return 1
            
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    adj_matrix = []
    for _ in range(N):
        adj_matrix.append(list(map(int, input().strip())))

    result = mazerun(N, adj_matrix)
    print(f'#{tc} {result}')
