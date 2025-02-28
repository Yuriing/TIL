import sys
sys.stdin = open('input1860.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N은 예약 손님 수, M은 붕어빵을 만드는 데 걸리는 시간, K는 M초마다 만들어지는 붕어빵 개수
    people = list(map(int, input().split()))  # 예약 손님이 방문하시게 될 초 리스트

    people.sort()  # 손님 도착 시간 오름차순 정렬
    possible = True  # 가능한지 여부를 저장할 변수

    for i in range(N):
        time = people[i]  # i번째 손님의 도착 시간
        produced = (time // M) * K  # 해당 시간까지 생산된 붕어빵 개수
        if produced < i + 1:  # 현재까지 온 손님 수보다 붕어빵이 부족하면
            possible = False
            break

    result = "Possible" if possible else "Impossible"
    print(f"#{tc} {result}")

# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())  # N은 예약 손님 수, M은 붕어빵을 만드는 데 걸리는 시간, K는 M초마다 만들어지는 붕어빵 개수
#     people = list(map(int, input().split()))  # 예약 손님이 방문하시게 될 초 리스트
#
#     people.sort()
#     people_copy = people.copy()
#
#     count = 0
#
#     while count >= 0:  # count 가 0보다 작아지는 순간 루프문 종료
#         for i in range(1, max(people)+1):  # 초 세기
#             for person in people:  # person초에 방문한 손님
#                 if i % M == 0:
#                     count += K  # M초마다 붕어빵 K개씩 생산
#
#                 if i == person:  # person초에 손님 방문
#                     count -= 1  # 붕어빵 1개씩 사감
#                     people_copy.pop(people_copy.index(i))  # 사간 손님 삭제
#
#     if len(people_copy) >= 0:  # 루프문이 끝났는데 아직 손님이 남아있다
#         print('Impossible')  # 실패
#     else:  # 루프문이 끝났을 때 손님이 안 계신다
#         print('Possible')  # 성공
