arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 집합 코드 복습
# 가지치기는 어떤 것이 있을까

# answer = []
# for i in range(1 << len(arr)):
#     lst = []
#     for j in range(len(arr)):
#         if i & (1 << j):
#             lst.append(arr[j])
#         if sum(lst) > 10:
#             break
#     if sum(lst) == 10:
#         answer.append(lst)
#
# print(answer)

# 재귀호출

# level: N개의 원소를 모두 고려하면
# branch: 집합에 해당 원소를 포함시키는 경우 or 안 시키는 경우
# 누적값
#   부분집합의 총합
#   부분집합에 포함된 원소들


def dfs(cnt, total, subset):
    if total == 10:
        return subset
    # total > 10 이면 가지치기
    if total > 10:
        return
    # total == 10 이면 출력
    if cnt == 10:
        return subset

    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])  # 포함하는 경우
    dfs(cnt + 1, total, subset)  # 안 하는 경우


print(dfs(0, 0, []))
