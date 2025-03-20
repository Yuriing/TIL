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
# 크루스칼
# 모든 간선들을 보면서
# 가중치가 가장 작은 간선부터 고르자(정렬)
# 이때 사이클이 발생한다면 넘어가기


def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return find_set(parents[x])


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


V, E = map(int, input().split())
edge = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((u, v, w))

edge.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬
parents = [i for i in range(V)]  # make_set(정점 기준)

# 작은 것부터 고르기
# n-1개를 선택할 때까지
cnt = 0
result = 0  # MST 가중치의 합

for u, v, w in edge:
    # u와 v가 연결이 안 되어있으면 선택
    # == 다른 집합이라면
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:  # MST 구성이 끝났다
            break

print(result)
