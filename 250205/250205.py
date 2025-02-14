def BubbleSort(arr) : 	# 정렬할 List
    N = len(arr)
    for i in range(N-1, 0, -1) : # 범위의 끝 위치
        for j in range(i) :		# 비교할 왼쪽 원소 인덱스 j
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = list(map(int, input().split(",")))
sorted_arr = BubbleSort(arr)
print(arr)

def bubble_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = list(map(int, input().split()))
print(bubble_sort(arr))






def subtraction(arr):
    N = len(arr)
    max_v = arr[0]  # 첫 원소를 최대값으로 가정
    min_v = arr[0]  # 첫 원소를 최소값으로 가정
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
            '''
            arr[1]부터 비교하여 max_v가 arr[1]보다 작을 경우
            max_v의 값을 arr[1]로 교체
            해당 동작을 arr 리스트의 인덱스 값 -1까지 반복
            '''
        if min_v > arr[i]:
            min_v = arr[i]
            '''
            arr[1]부터 비교하여 min_v가 arr[1]보다 클 경우
            min_v의 값을 arr[1]로 교체
            해당 동작을 arr 리스트의 인덱스 값 -1까지 반복
            '''
    return max_v - min_v

arr_1 = list(map(int, input().split()))
print(subtraction(arr_1))