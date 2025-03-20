import sys
sys.stdin = open('input5251.txt')
import heapq

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())  # 시작, 끝, 거리
        graph[u].append((v, w))

    pq = [(0, 0)]
    dists = [float('inf')] * (N+1)
    dists[0] = 0

    while pq:
        node, dist = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_node, next_dist = next_info

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (next_node, next_dist))

    print(f'#{tc} {dists[N]}')
