import sys
sys.stdin = open('input4485.txt')
import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(r, c):
    pq = [(matrix[r][c], r, c)]
    dists = [[float('inf')] * N for _ in range(N)]
    dists[r][c] = matrix[r][c]

    while pq:
        dist, r, c = heapq.heappop(pq)

        if dists[r][c] < dist:
            continue

        for i in range(4):
            if 0 <= r+dr[i] < N and 0 <= c+dc[i] < N:
                nr = r + dr[i]
                nc = c + dc[i]

                new_dist = matrix[nr][nc] + dist

                if dists[nr][nc] > new_dist:
                    dists[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))

    return dists[N-1][N-1]


tc = 1
while True:
    N = int(input())

    if N == 0:
        break

    else:
        matrix = [list(map(int, input().split())) for _ in range(N)]

        answer = dijkstra(0, 0)
        print(f'Problem {tc}: {answer}')

        tc += 1

