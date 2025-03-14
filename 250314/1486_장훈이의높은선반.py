import sys
sys.stdin = open('input1486.txt')


def tower(arr, count, height, B):
    global answer
    if height >= B:
        answer = min(answer, height)
        return

    if count == len(arr):
        return

    tower(arr, count+1, height+arr[count], B)
    tower(arr, count+1, height, B)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())

    arr = list(map(int, input().split()))

    answer = float('inf')
    tower(arr, 0, 0, B)

    print(f'#{tc} {answer - B}')
