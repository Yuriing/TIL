import sys
sys.stdin = open('input20551.txt')

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0
    if B >= C:
        cnt += B - C + 1
        B = C -1

    if A >= B:
        cnt += A - B + 1
        A = B - 1

    if A <= 0 or B <= 0:
        print(f'#{tc} -1')

    else:
        print(f'#{tc} {cnt}')
