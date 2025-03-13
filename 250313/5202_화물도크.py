import sys
sys.stdin = open('input5202.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])

    # 완료 시각 순으로 arr을 정렬한다.
    # 버블 정렬 사용
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    b = arr[0][1]  # 종료 시각
    start = 1
    cnt = 1
    now = True
    while now:

        if b == 24:  # 화물차의 완료 시각이 마지막 타임일 때
            break

        if start == N:  # 모든 신청서의 시각을 확인했을 때
            break

        for i in range(start, N):  # 현재 화물차 다음 신청서부터 확인
            if arr[i][0] - b >= 0:  # 시작 시각이 종료 시각과 같거나 클때
                b = arr[i][1]  # 현재 화물차 갱신
                start = i + 1  # 확인할 신청서 범위 갱신
                cnt += 1
                break

        else:  # 뒤로 신청서가 남았지만 더 이상 신청을 받아줄 수 없을 때
            break

    print(f'#{tc} {cnt}')

