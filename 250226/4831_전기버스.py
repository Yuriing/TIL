import sys
sys.stdin = open('input4831.txt')

T = int(input())
for tc in range(1, T+1):

    K, N, M = map(int, input().split())
    bus_stop = [0] * (N+1)

    charge = list(map(int, input().split()))

    for i in range(N+1):
        for num in charge:
            if i == num:
                bus_stop[i] = 1

    now = 0
    count = 0
    while now < N+1:
        if now + K >= N:
            count = count
            break
        for n in range(K, 0, -1):
            if now+n < N+1 and bus_stop[now+n] == 1:
                now += n
                count += 1
                break
            elif now+n < N+1 and bus_stop[now+n] == 1:
                continue
        else:
            count = 0
            break

    print(f'#{tc} {count}')
