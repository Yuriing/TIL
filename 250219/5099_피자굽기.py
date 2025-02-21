# import sys
# sys.stdin = open('input5099.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     pizza_lst = list(map(int, input().split()))
#
#     oven = []
#     if len(pizza_lst) > 0:
#         for i in range(N):
#             oven.append(pizza_lst.pop(0))
#
#     while set(oven) != {0, 1}:
#         # oven 속 모든 cheese 에 대하여 //2
#         # oven 속 cheese 숫자가 한 바퀴 이후 리셋되는 문제
#
#         for i in range(len(oven)):
#             oven[i] = oven[i] // 2
#
#             # 피자 한 판의 치즈가 전부 녹았을 경우
#             if oven[i] == 0:
#                 # 아직 돌릴 피자가 남아있을 경우
#                 if len(pizza_lst) > 0:
#                     # 피자 교체
#                     while 0 in oven:
#                         oven.pop(oven.index(0))
#                         oven.append(pizza_lst.pop(0))
#             else:
#                 continue
#
#     print()

import sys
sys.stdin = open('input5099.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza_lst = list(enumerate(map(int, input().split()), start=1))  # (피자 번호, 치즈량)

    oven = pizza_lst[:N]
    pizza_lst = pizza_lst[N:]

    while len(oven) > 1:  # 피자가 하나 남을 때까지
        pizza_num, cheese = oven.pop(0)  # 가장 앞에 있는 피자 꺼내기
        cheese = cheese // 2  # 치즈 양 줄이기

        if cheese == 0:  # 치즈가 다 녹았을 경우
            if pizza_lst:  # 남은 피자가 있다면 새 피자 투입
                oven.append(pizza_lst.pop(0))
        else:
            oven.append((pizza_num, cheese))  # 치즈가 남아있다면 다시 오븐에 넣기

    print(f"#{tc} {oven[0][0]}")


