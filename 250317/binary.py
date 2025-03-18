arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용해야 한다
arr.sort()


def binary_search_while(target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # 왼쪽에 정답이 있다
        if target < arr[mid]:
            right = mid - 1
        else:  # 오른쪽에 정답이 있다
            left = mid + 1

    return -1


def binary_search_recur(left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)
    else:
        return binary_search_recur(mid + 1, right, target)



