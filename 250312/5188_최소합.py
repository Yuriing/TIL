import sys
sys.stdin = open('input5188.txt')

# 델타 우 하
dr = [0, 1]
dc = [1, 0]

def permute(arr, depth, result, visited, lst):
    if depth == len(arr):
        lst.append(list(tuple(result)))

    for i in range(len(arr)):
        if not visited[i]:
            # 같은 숫자가 연속적으로 중복 사용되는 것을 방지
            if i > 0 and arr[i] == arr[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            result.append(arr[i])
            permute(arr, depth + 1, result, visited, lst)
            result.pop()
            visited[i] = False
    return lst


# 나열한 방향대로 진행하며 합을 구하는 함수
def plus_matrix(matrix, direction, sums):

    for row in direction:
        sum_v = matrix[0][0]
        r = 0
        c = 0
        for i in row:
            if 0 <= r+dr[i] < N and 0 <= c+dc[i] < N:
                r += dr[i]
                c += dc[i]
                sum_v += matrix[r][c]
        sums.append(sum_v)
    return min(sums)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 필요한 방향은 오른쪽 (N-1)번, 아래쪽 (N-1)번
    arr = [0]*(N-1) + [1]*(N-1)

    # 오른쪽과 아래쪽을 나열한 모든 경우의 수 도출
    visited = [False] * (len(arr))
    lst = []
    direction = permute(arr, 0, [], visited, lst)

    # 방향을 나열한 경우의 수대로 진행하여 얻은 합들의 최소값 도출
    result = plus_matrix(matrix, direction, [])

    print(f'#{tc} {result}')


# from itertools import permutations
#
# # 방향 벡터: 우(0), 하(1)
# dr = [0, 1]
# dc = [1, 0]
#
# def plus_matrix(matrix, direction, N):
#     sums = []
#     for row in direction:
#         sum_v = matrix[0][0]
#         r, c = 0, 0
#         for i in row:
#             nr, nc = r + dr[i], c + dc[i]
#             if 0 <= nr < N and 0 <= nc < N:
#                 r, c = nr, nc
#                 sum_v += matrix[r][c]
#         sums.append(sum_v)
#     return min(sums)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#
#     # 가능한 방향 조합 (0: 오른쪽, 1: 아래쪽)
#     arr = [0] * (N-1) + [1] * (N-1)
#
#     # 방향 조합을 모든 순열로 생성 (중복 제거)
#     direction = list(set(permutations(arr, len(arr))))
#
#     # 최소 합 계산
#     result = plus_matrix(matrix, direction, N)
#
#     print(f'#{tc} {result}')
