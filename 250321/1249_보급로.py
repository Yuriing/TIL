import sys
sys.stdin = open('input1249.txt')
import heapq
'''
출발점(0, 0) 부터 갈 수 있는 곳을 모두 갈 수 있는 후보 리스트에 넣는다
후보 리스트 중 가장 적은 시간이 걸리는 곳부터 먼저 탐색한다
    리스트에서 가장 적은 시간이 걸리는 위치를 먼저 꺼내야 한다
    즉, 우선순위 큐를 사용해야 한다.
특정 위치까지 간 거리들을 계속 저장하면서 나아간다
전체 탐색이 완료되거나, 도착지(N-1, N-1) 좌표로 도착하면 중지한다
'''

# 전형적인 다익스트라 문제
# 최단거리를 저장할 dists 배열을 이차원 리스트로 만들어야 한다

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# N = int(input())
# graph = [list(map(int, input().strip())) for _ in range(N)]
#
#
# def dijkstra():
#     dists = [[float('inf')] * N for _ in range(N)]
#     dists[0][0] = 0
#
#     pq = [(0, 0, 0)]
#
#     while pq:
#         dist, y, x = heapq.heappop(pq)
#
#         for i in range(4):
#             new_y = y + dy[i]
#             new_x = x + dx[i]
#
#             if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
#                 continue


def dijkstra(r, c):
    pq = [(0, r, c)]
    dists = [[float('inf')] * N for _ in range(N)]
    dists[r][c] = 0

    while pq:
        dist, r, c = heapq.heappop(pq)
        if dists[r][c] < dist:
            continue

        for i in range(4):
            if 0 <= r + dr[i] < N and 0 <= c + dc[i] < N:
                nr = r + dr[i]
                nc = c + dc[i]

                new_dist = matrix[nr][nc] + dist

                if dists[nr][nc] > new_dist:
                    dists[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))

    result = min(dists[N-2][N-1], dists[N-1][N-2])
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]

    answer = dijkstra(0, 0)
    print(f'#{tc} {answer}')
