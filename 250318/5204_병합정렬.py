import sys
sys.stdin = open('input5204.txt')


def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = 0
    r = 0
    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result


def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_lst = arr[:mid]
    right_lst = arr[mid:]

    return merge(merge_sort(left_lst), merge_sort(right_lst))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')
