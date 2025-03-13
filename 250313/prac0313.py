'''

'''
'''
민철이에게는 세 명의 친구가 있다.
['MIN', 'CO', 'TIM']
함께 영화관에 갈 수 있는 멤버를 구성하고자 한다
모든 경우를 출력해보자
'''
# arr = ['O', 'X']
# path = []
# name = ['MIN', 'CO', 'TIM']
#
#
# def print_name():
#     print('{', end=' ')
#     for i in range(3):
#         if path[i] == 'O':
#             print(name[i], end=' ')
#     print('}')
#


def recur():
    pass
    '''
    if 3명을 판단했으면:
        print_name()
        return

    recur(포함하는 경우)

    recur(포함하지 않는 경우)
    '''
# friend = ['A', 'B', 'C', 'D', 'E']
#
# count = 0
# for i in range(1<<len(friend)):
#     arr = []
#     for j in range(len(friend)):
#         if i & (1<<j):
#             arr.append(friend[j])
#     if len(arr) >= 2:
#         count += 1
#
# print(count)
'''
1인 bit 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    for _ in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1

    return cnt
'''
'''
for 문으로 조합 구현하기
'''
# arr = ['A', 'B', 'C', 'D', 'E']
#
# for a in range(5):  # 첫번째 고르기
#     start1 = a + 1
#     for b in range(start1, 5):  # 첫번째 고르고 그 다음 중에서 하나 고르기
#         start2 = b + 1
#         for c in range(start2, 5):  # 두번째 고르고 그 다음 중에서 하나 고르기
#             print(arr[a], arr[b], arr[c])
#
'''
또 다른 방법
'''
# n = 3
# path = []
#
# # 5명 중 3명 뽑기
# def recur(cnt, start):
#     if cnt == n:  # n명을 뽑을면 종료
#         print(*path)
#         return
#
#     # 5명을 고려해야 한다
#     for i in range(start, len(arr)):
#         path.append(arr[i])
#         recur(cnt+1, i+1)  # start 변경해서 넘겨주기
#         path.pop()
#
#
# recur(0, 0)

'''
주사위 던지기
'''
# path2 = []
# def diceroll(cnt, start):
#     if cnt == 3:
#         print(path2)
#         return
#
#     for i in range(start, 7):
#         path2.append(i)
#         diceroll(cnt+1, i)
#         path2.pop()
#
#
# diceroll(0, 1)
'''
동전문제
'''
# coin_list = [500, 100, 50, 10]
# target = 1730
# cnt = 0
#
# for coin in coin_list:
#     possible_cnt = target // coin
#     cnt += possible_cnt
#     target -= coin * possible_cnt
# print(cnt)
'''
화장실 문제
짧게 쓰는 사람부터 집어넣는다
'''
# people = [15, 30, 50, 10]
# n = len(people)
#
# people.sort()  # 오름차순 정렬
# total_time = 0  # 전체 시간
# remain_people = n - 1 # 대기 인원 수
#
# for turn in range(n):
#     time = people[turn]
#     total_time += time * remain_people
#     remain_people -= 1
#
# print(total_time)
#
'''
연습문제
아래 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 부분 집합을 모두 출력하시오.
[-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
'''

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

for i in range(1<<len(arr)):
    lst = []
    for j in range(len(arr)):
        if i & (1<<j):
            lst.append(arr[j])
    if sum(lst) == 0:
        print(lst)

