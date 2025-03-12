import sys
sys.stdin = open('input10580.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    wires = []
    cnt = 0
    for _ in range(N):
        A, B = map(int, input().split())

        for prev_A, prev_B in wires:
            if prev_A > A and prev_B < B:
                cnt += 1

            if prev_A < A and prev_B > B:
                cnt += 1

        wires.append((A, B))

    print(f'#{tc} {cnt}')
