'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * V
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:  # 이미 더 작은 경로로 온 적이 있다면 지나치기
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            # 다음 노드로 가기 위한 누적 거리 계산
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:  # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면
                continue

            dists[next_node] = new_dist  # next_node 까지 도착하는 데 비용은 new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists


import heapq
INF = float('inf')

V, E = map(int, input().split())
start_node = 0
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # 단방향 그래프

# 0에서 출발해서 다른 노드들까지의 최단 거리를 모두 구한다
result_dists = dijkstra(0)
print(result_dists)
