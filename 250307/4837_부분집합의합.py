import sys
sys.stdin = open('input4837.txt')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    lst = []
    for i in range(1 << 12):
        arr = []
        for j in range(12):
            if i & (1 << j):
                arr.append(A[j])
        lst.append(arr)

    count = 0
    for arr in lst:
        if len(arr) == N and sum(arr) == K:
            count += 1

    print(f'#{tc} {count}')
