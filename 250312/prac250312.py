'''
'''

'''
반복과 재귀
반복은 수행하는 작업이 완료될 때까지 반복

재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
재귀호출은 n 중 반복문을 만들어낼 수 있다.
'''
# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for h in range(1, 4):
#                 print(f'{i} {j} {k} {h}', end=", ")
#
# path = []
# N = 3
# #
# #
# def run(lev):
#     if lev == N:
#         print(path)
#         return
#
#     for i in range(1, 4):
#         path.append(i)
#         run(lev + 1)
#         path.pop()
#
#
# run(0)
#
#
# def BBQ(x):
#     x += 10
#     print(x)
#
# def KFC(x):
#     print(x)
#     x += 3
#     BBQ(x+2)
#     print(x)
#
#
# x = 3
# KFC(x+1)
# print(x)


# def KFC(num):
#     # 언제 끝낼까?
#     if num == 5:
#         return
#
#     # 재귀 호출 전 들어가야 할 로직
#     print(num)
#     KFC(num+1)  # 다음 재귀 호출(매개변수를 변경하면서 전달)
#     print(num)  # 돌아오면서 해야 할 로직
#
#
# KFC(0)
# print('끝')


# # [0, 1, 2] 3 개의 카드 존재
# # 2개를 뽑을 예정
#
# #뽑은 카드 저장
# path = []
# # cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
# def recur(cnt):
#     # 카드를 두 장 뽑으면 종료
#     if cnt == 3:  # 종료 시에 해야 할 로직 작성
#         print(*path)
#         return
#
#     for num in range(1, 7):
#         path.append(num)
#         recur(cnt+1)
#         path.pop()
#
#     # # 카드를 뽑는다
#     # path.append(0)
#     # # 다음 재귀 호출(뽑은 카드가 한 장 추가되었음)
#     # recur(cnt+1)
#     # path.pop()
#     #
#     # # 카드를 뽑는다
#     # path.append(1)
#     # # 다음 재귀 호출(뽑은 카드가 한 장 추가되었음)
#     # recur(cnt+1)
#     # path.pop()
#     #
#     # # 카드를 뽑는다
#     # path.append(2)
#     # # 다음 재귀 호출(뽑은 카드가 한 장 추가되었음)
#     # recur(cnt+1)
#     # path.pop()
#
#
# # 제일 처음 호출할 때 시점
# # 초기값을 전달하며 시작
# recur(0)


# path2 = []
# used = [False] * 7  # 1~6 숫자 사용 여부 기록
#
# # 조금 더 어려운 문제의 경우(숫자 범위가 매우 커서 메모리 초과 가능성이 있다면)
# # 딕셔너리나 셋으로 해결
#
# # cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
# def recur2(cnt):
#     # 카드를 두 장 뽑으면 종료
#     if cnt == 3:  # 종료 시에 해야 할 로직 작성
#         print(*path2)
#         return
#
#     for num in range(1, 7):
#         # # 이미 num을 뽑았다면 뽑지 마라
#         # # num을 뽑지 않았을 때만 뽑아라
#         # if num in path:
#         #     continue
#         if used[num] is True:
#             continue
#
#         used[num] = True
#         path2.append(num)
#         recur2(cnt+1)
#         path2.pop()
#         used[num] = False
#
#
# recur2(0)

'''
주사위 3개를 던져 합이 10 이하인 경우
종료 조건: 3번 던진다
나올 수 있는 범위: 1~6
중복 순열
'''

# path3 = []
# result = 0
# def recur3(cnt, total):
#     global result
#     if total > 10:  # 이미 10을 넘으면 더 볼 필요가 없다
#         return
#
#     # 합이 10 이하인 건 몇 개???
#     if cnt == 3:
#         # if sum(path3) <= 10:
#         #     result += 1
#         if total <= 10:
#             result += 1
#             print(path3)
#         return
#
#     for num in range(1, 7):
#         path3.append(num)
#         recur3(cnt+1, total+num)
#         path3.pop()
#
#     return result
#
#
# print(recur3(0, 0))

'''
연속 3장의 트럼프카드
'''
# card = ['A', 'J', 'Q', 'K']
# path = []
# result2 = 0
#
# def count_three():
#     if path[0] == path[1] == path[2]: return True
#     if path[1] == path[2] == path[3]: return True
#     if path[2] == path[3] == path[4]: return True
#     return False
#
#
# def recur4(cnt):
#     global result2
#     if cnt == 5:
#         # 연속 3개가 나오면 counting
#         if count_three():
#             result2 += 1
#             print(path)
#         return
#
#     for idx in range(4):
#         path.append(card[idx])
#         recur4(cnt+1)
#         path.pop()
#
#
# recur4(0)


# 전체를 보자
# 끝날 때 무언가를 하라
# 중복 제거하라
'''
baby-gin(완전탐색으로)
6자리 숫자를 입력
숫자 3개가 연속되었는가
숫자 3개가 같은가
순열로 처리

6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

# used = [0] * 6
# path5 = []
# baby_gin_result = False
#
#
# def is_baby_gin():
#     cnt = 0
#     a, b, c = path5[0], path5[1], path5[2]
#     if a == b == c:
#         cnt += 1
#     elif a == (b-1) == (c-2):
#         cnt += 1
#
#     a, b, c = path5[3], path5[4], path5[5]
#     if a == b == c:
#         cnt += 1
#     elif a == (b - 1) == (c - 2):
#         cnt += 1
#
#     return cnt == 2
#
#
# def recur5(cnt):
#     global baby_gin_result
#     if cnt == 6:
#         if is_baby_gin():
#             baby_gin_result = True
#         return
#
#     for i in range(6):
#         # 인덱스를 이미 썼다면 뽑지 말아야 함
#         if used[i]:
#             continue
#         used[i] = 1
#         path5.append(arr[i])
#         recur5(cnt+1)
#         path5.pop()
#         used[i] = 0
#
#
# arr = list(map(int, input().split()))
# recur5(0)
#
# if baby_gin_result == True:
#     print('Yes')
# else:
#     print('No')

'''
중복... 이걸 뭐라고 하더라
'''


def permute(arr, depth, result, visited, lst):
    if depth == len(arr):
        lst.append(list(result))  # 튜플 형태로 출력 (집합으로 중복 제거 가능)

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


# 정렬된 리스트 사용 (중복 방지를 위함)
arr = [0, 0, 1, 1]
arr.sort()  # 같은 숫자가 있을 때 중복을 방지하기 위해 정렬
visited = [False] * len(arr)
lst = []

print(permute(arr, 0, [], visited, lst))

