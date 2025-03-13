import sys
sys.stdin = open('input4012.txt')


def for_perfectcook(arr, n):
    lst = []

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in for_perfectcook(arr[i+1:], n-1):
            result1 = [elem] + rest
            result2 = list(set(arr) - set(result1))
            lst.append([result1, result2])

    return lst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    arr = [i for i in range(1, N+1)]

    lst = for_perfectcook(arr, N//2)

    print(f'#{tc} {lst}')
