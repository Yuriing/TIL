import sys
sys.stdin = open('input4871.txt')

def find_node(S, G, V, adj_matrix):
    visited = [0]*(V+1)
    stack = []

    stack.append(S)

    while stack:
        current_node = stack.pop()
        if current_node == G:
            return 1

        if visited[current_node] == 0:
            visited[current_node] = 1

            for next_node in range(V, 0, -1):
                if adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                    stack.append(next_node)

    return 0


T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        n, m = map(int, input().split())
        adj_matrix[n][m] = 1
        # adj_matrix[m][n] = 1

    S, G = map(int, input().split())

    result = find_node(S, G, V, adj_matrix)

    print(f'#{tc} {result}')