# '''
# '''
# '''
# prim
# '''
# import heapq
#
#
# def prim(tax):
#     pq = [(0, 0)]
#     visited = [0] * N
#     min_cost = 0
#
#     dists = [float('inf')] * N
#     dists[0] = 0
#
#     while pq:
#         cost, node = heapq.heappop(pq)
#
#         if visited[node]:
#             continue
#
#         # node 로 가는 간선을 확정짓는 코드
#         visited[node] = 1
#         min_cost += cost
#
#         for next_node in range(N):
#             if visited[next_node]:
#                 continue
#
#             new_cost = ((x_list[next_node] - x_list[node]) ** 2 + (y_list[next_node] - y_list[node]) ** 2) * tax
#
#             if new_cost < dists[next_node]:
#                 dists[next_node] = new_cost
#                 heapq.heappush(pq, (new_cost, next_node))
#
#
# N = int(input())
# x_list = list(map(int, input().split()))  # x 좌표
# y_list = list(map(int, input().split()))  # y 좌표
# tax = float(input())
#
#
# '''
# kruskal
# 간선 위주 알고리즈
# 간선들을 정렬하고 최소 간선들을 뽑아야 한다
# 사이클 검사가 동반되어야 한다
# '''
#
#
# def find_set(x):
#     if x == parents[x]:
#         return x
#
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
#
# def union(x, y):
#     ref_x = find_set(x)
#     ref_y = find_set(y)
#
#     if ref_x < ref_y:
#         parents[ref_y] = ref_x
#     else:
#         parents[ref_x] = ref_y
#
#
# edges = []
# for i in range(N):
#     for j in range(N):
#         cost = ((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2) * tax
#
# edges.sort(key=lambda x: x[2])
#
# parents = [i for i in range(N)]
#
# count = 0
# for u, v, w in edges:
#     if find_set(u) != find_set(v):
#         union(u, v)
#         min_cost += w
#         count += 1
#     if count == N-1:
#         break
import sys
sys.stdin = open('input1251.txt')
import heapq


def prim(start, tax):
    pq = [(0, start)]
    MST = [0] * N
    charge = 0

    dists = [float('inf')] * N
    dists[start] = 0

    while pq:
        cost, idx = heapq.heappop(pq)

        if MST[idx] == 1:
            continue

        MST[idx] = 1
        charge += cost

        for next_island in range(N):
            if MST[next_island] != 1:
                new_cost = (((x_point[idx] - x_point[next_island]) ** 2) + ((y_point[idx] - y_point[next_island]) ** 2)) * tax

                if new_cost < dists[next_island]:
                    dists[next_island] = new_cost
                    heapq.heappush(pq, (new_cost, next_island))

    return charge


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    x_point = list(map(int, input().split()))
    y_point = list(map(int, input().split()))

    tax = float(input())

    print(f'#{tc} {round(prim(0, tax))}')
