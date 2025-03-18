def partition(left, right):
    pivot = arr[left]  # 왼쪽 끝을 피봇으로 설정

    i = left + 1  # 왼쪽 다음부터
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:  # 피봇보다 큰 값을 찾기 전까지
            i += 1  # 한 칸씩 전진

        while i <= j and arr[j] >= pivot:  # 피봇보다 작은 값을 찾기 전까지
            j -= 1  # 한 칸씩 후진

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(left, right):
    if left < right:
        pivot = partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
print(arr)
