import sys
sys.stdin = open('input5247.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 시작점을 N으로 하는 BFS
    q = [(N, 0)]
    visited = set([N])
    print(f'#{tc}', end=" ")
    while q:
        current, cnt = q.pop(0)

        for next in [current+1, current-1, current*2, current-10]:
            if next == M:
                print(cnt+1)  # 여기서 연산을 한 번 더 한 것이므로 +1을 하고 종료
                break
            elif next not in visited and next <= 1000000:
                q.append((next, cnt+1))
                visited |= {next}
        if next == M:
            break
