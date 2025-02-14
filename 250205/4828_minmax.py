import sys
sys.stdin = open('input4828.txt')

def subtraction(N, arr):
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


T = int(input())
for n in range(1, T+1):
    N = int(input())
    arr_1 = list(map(int, input().split()))
    print(f'#{n} {subtraction(N, arr_1)}')