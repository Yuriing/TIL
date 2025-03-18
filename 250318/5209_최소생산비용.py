import sys
sys.stdin = open('input5209.txt')
'''
r: 공장의 인덱스 번호
cost: 현재까지 계산한 총생산비용
visited: 이전에 고른 제품 번호를 담아두는 리스트
'''


def production(r, cost, visited, min_cost):
    if r == N:  # 모든 공장을 다 돌아봤을 경우
        return min(min_cost, cost)

    # 현재까지 계산한 총생산비용이 이전에 구한 최소생산비용보다 클 경우 가지를 쳐낸다
    if cost > min_cost:
        return min_cost

    for i in range(N):  # 공장마다 돌면서 제품을 하나씩 고른다
        if i not in visited:  # 단, 이전에 들른 공장에서 이미 고른 제품은 제외
            min_cost = production(r+1, cost + matrix[r][i], visited + [i], min_cost)

    return min_cost


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 행과 열의 위치를 바꾼다
    # 한 공장을 한 행으로 묶어두는 게 더 편해서...
    for r in range(N):
        for c in range(N):
            if r < c:
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    result = production(0, 0, [], float('inf'))

    print(f'#{tc} {result}')
