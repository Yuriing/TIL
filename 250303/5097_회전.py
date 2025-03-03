import sys
sys.stdin = open('input5097.txt')

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    for _ in range(M):

        num = lst.pop(0)
        lst.append(num)

    result = lst.pop(0)

    print(f'#{tc} {result}')