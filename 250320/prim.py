'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# prim
# 특정 정점을 기준으로 시작
# 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 고르자
# 그냥 큐가 아닌 우선순위 큐 활용

import heapq


def prim(start_node):
    pq = [(0, start_node)]  # 시작점은 가중치가 0이다
    MST = [0] * V  # visited 랑 동일
    min_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if MST[node]:  # 한 번 간 곳은 다른 간선을 통하더라도 가지 않는다
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V):
            if graph[node][next_node] == 0:
                continue

            if MST[next_node] == 1:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))

    return min_weight


V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]  # 인접 행렬

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

result = prim(0)  # 정점을 바꿔도 결과가 동일함
print(f'최소비용: {result}')
