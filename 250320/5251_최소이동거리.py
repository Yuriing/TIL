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
        dist, node = heapq.heappop(pq)  # 우선순위 큐이기 때문에 거리 먼저 저장

        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_node, next_dist = next_info

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    print(f'#{tc} {dists[N]}')  # N번을 인덱스 넘버로 삼아 출력
