import sys
sys.stdin = open('input5102.txt')


def howtogo(S, G):
    visited = [0] * (V+1)
    q = []
    q.append(S)
    visited[S] = 1

    while q:
        current_node = q.pop(0)

        if current_node == G:
            return visited[current_node] - 1

        for next_node in range(V+1):
            if adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                q.append(next_node)
                visited[next_node] = visited[current_node] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2 = map(int, input().split())
        adj_matrix[n1][n2] = 1
        adj_matrix[n2][n1] = 1

    S, G = map(int, input().split())

    print(f'#{tc} {howtogo(S, G)}')

# def howtogo(S, G):
#     visited = [0] * (V+1)
#     q = []
#
#     visited[S] = 1
#     q.append(S)
#
#     count = 0
#
#     while q:
#         current_node = q.pop()
#
#         if current_node == G:
#             return count
#
#         for next_node in adj_list[current_node]:
#             if visited[next_node] == 0:
#                 visited[next_node] = visited[current_node] + 1
#                 q.append(next_node)
#                 count += 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#
#     adj_list = [[] for _ in range(V + 1)]
#
#     # 간선 정보를 바탕으로 인접 리스트에 기록(무방향)
#     for i in range(E):
#         n1, n2 = map(int, input().split())
#         adj_list[n1].append(n2)
#         adj_list[n2].append(n1)
#
#     # 방문 시 작은 번호부터 접근하기 위해 각 간선정보 리스트를 오름차순으로 정렬
#     for i in range(1, V + 1):
#         adj_list[i].sort()
