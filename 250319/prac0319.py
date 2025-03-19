# ''''''
# '''
# 7 8
# 1 2
# 1 3
# 2 4
# 2 6
# 4 6
# 5 6
# 6 7
# 3 7
# '''
#
#
# def dfs(node):
#     # for 문을 돌며 끝나기 때문에 종료조건이 따로 없는 경우가 많음
#
#     # 가지치기
#     # K개의 노드를 모두 방문했다면 종료...
#     # N개를 모두 방문했다면 경로 출력...
#
#     print(node, end=" ")
#     visited[node] = 1
#
#     # 내가 갈 수 있는 후보들을(현재 노드에서 인접한 노드들) 모두 확인하면서 한 군데로 진행
#     for next_node in graph2[node]:
#         if visited[next_node]:
#             continue
#
#         visited[next_node] = 1
#         dfs(next_node)
#
#
# def bfs(start_node):
#     # q: 다음에 방문해야 할 노드들의 대기열
#     q = [start_node]
#
#     while q:
#         # 가장 앞에 있는 데이터를 뽑는다
#         now = q.pop(0)
#         print(now, end=" ")
#
#         # 해당 노드에서 갈 수 있는 노드들을 큐에 넣는다
#         for next_node in graph2[now]:
#             if visited[next_node]:
#                 continue
#
#             visited[next_node] = 1
#             q.append(next_node)
#
#
# N, M = map(int, input().split())
#
# # 그래프를 저장하기
# # 비어있는 그래프 생성
# # 그래프 정보를 입력받는다
#
# # 인접 행렬(N*N의 0 배열)
# graph1 = [[0] * (N+1) for _ in range(N+1)]
# # 인접 리스트(N*N의 [] 배열)
# graph2 = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     s, e = map(int, input().split())
#     graph2[s].append(e)
#     graph2[e].append(s)  # 양방향이면 뒤집어서 다시 한 번 더 저장해줘야 한다
#
# visited = [0] * (N+1)  # 방문 여부 기록
# dfs(1)


def make_set(x):
    # 1~n개의 원소가 있다고 가정
    # 총 n개의 집합을 생성
    parents = [i for i in range(N+1)]
    ranks = [0] * (n+1)  # rank를 모두 0으로 초기화
    return parents, ranks


def find_set(x):
    # # 자신 == 부모노드 > 해당 집합의 대표자다
    # if parents[x] == x:
    #     return x
    #
    # # 경로 압축 추가(path compression)
    # # 부모를 대표자로 변경하는 과정
    # parents[x] = find_set(parents[x])  # 대표자를 찾아오는 재귀호출
    #
    # # x의 부모노드를 기준으로 다시 대표자를 검색
    # return parents[x]

    # 할 때마다 모든 노드의 대표자를 변경하자
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
        return x


def union(x, y):
    # x, y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면?
    if ref_x == ref_y:
        return  # 병합 안 해도 된다!

    # # 다른 집합이라면 합친다
    # # 문제에 따라 우선되는 집합으로 합쳐주면 됨
    # # 이번 예시에서는 더 작은 노드로 합친다
    # if ref_x < ref_y:
    #     parents[ref_y] = ref_x
    # else:
    #     parents[ref_x] = ref_y

    # rank가 작은 쪽으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:  # 랭크가 같으면 한쪽으로 병합하고 병합한 쪽 대표자의 랭크 증가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


N = 6
parents, ranks = make_set(N)

# 3과 5는 같은 집합인가요?
# 대표자가 아니라 부모 노드를 기준으로 확인
if find_set(3) == find_set(5):
    print("같은 집합입니다!")
else:
    print("다른 집합입니다.")
