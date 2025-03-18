import sys
sys.stdin = open('input5208.txt')
'''
cnt: 충전 횟수
i: 버스 위치(인덱스 넘버)
'''


def electricbus(cnt, i):
    global N, min_cnt
    if i >= N:  # 버스의 현재 위치가 종점이거나 종점보다 더 나갔다면
        min_cnt = min(min_cnt, cnt)  # min_cnt 갱신
        return min_cnt  # 종료

    M = arr[i]  # 버스 현재 위치의 충전지 용량
    for m in range(M, 0, -1):  # 멀리에서부터 센다. 그래야 답이 빨리 나올 거 같아서...
        if cnt + 1 >= min_cnt:  # 만약 cnt가 최대 경우의 수에 도달했다면 함수 중지
            return
        electricbus(cnt + 1, i+m)  # 충전 횟수 +1, 버스 위치 갱신


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)  # 정류장 개수
    arr = [0] + arr + [0]  # 정류장. 주어지는 숫자를 그대로 인덱스 넘버로 활용하기 위해 [0] 추가

    min_cnt = N  # 모든 정류장을 들르는 경우를 최대 경우의 수로 삼고 이보다 작은 수를 찾으면 갱신한다
    electricbus(0, 1)
    print(f'#{tc} {min_cnt-1}')  # 출발지에서의 배터리 장착은 교환 횟수에서 제외
