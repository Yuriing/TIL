# # 01 이진탐색
# def find_book(page, find_page):
#     count = 0  # 책을 찾는 횟수 초기화
#     start = 1
#     end = page
#     while start <= end:
#         mid = int((start + end)/2)  # 문제에서 제시한 중간 페이지 계산식
#         count += 1  # 한 번 돌아올 때마다 횟수 추가
#         if mid == find_page:
#             return count
#         elif mid > find_page:
#             end = mid - 1
#         else:
#             start = mid + 1

#     return count


# def winner(A, B):  # A와 B 둘 중 이긴 사람 도출 함수
#     if A > B:
#         return 'B'
#     elif A == B:
#         return 0
#     else:
#         return 'A'
    
# lst = list(map(int, input().split()))
# # find_book에 인자를 리스트 인덱스로 전달
# A = find_book(lst[0], lst[1])
# B = find_book(lst[0], lst[2])
# print(winner(A, B))


# 02 특별한 정렬
# 버블정렬로 주어진 N개의 정수를 오름차순 나열
def special_sort(N, arr):
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 오른쪽, 왼쪽 선택을 반복
    new_arr = []
    for i in range(N):
        new_arr.append(arr[N - 1 - i])  # 리스트 맨 오른쪽 항목 반환
        if i != N:
            new_arr.append(arr[i])  # 리스트 맨 왼쪽 항목 반환

    # 새로운 리스트를 반으로 자름
    new_arr = new_arr[:len(new_arr)//2]

    # 리스트를 문자열 형태로 형변환하여 반환
    return " ".join(map(str, new_arr))

N = int(input())
arr = list(map(int, input().split()))
print(special_sort(N, arr))

# 03 달팽이 숫자
# N * N 형태의 이차원 배열 생성
N = int(input())
matrix = [[0] * N for _ in range(N)]

# 델타 설정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c = 0, 0  # r, c의 초기값
direction = 0  # direction의 초기값

for num in range(1, N+1):
    matrix[r][c] = num
    r += dr[direction]
    c += dc[direction]

for end in range(N - 1, 0, -1):
    for _ in range(2):
        direction = (direction + 1) % 4
        for _ in range(end):  
            r += dr[direction]
            c += dc[direction]
            num += 1
            matrix[r][c] = num
        

for row in matrix:
    print(row)



# # 04 숫자를 정렬하자
# ## 버블 정렬
# def bubble_sort(N, arr):
#     for i in range(N - 1):
#         for j in range(N - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return " ".join(map(str, arr))

# ## 선택 정렬
# def selection_sort(N, arr):
#     for i in range(N-1):
#         min_i = i
#         for j in range(i+1, N):
#             if arr[min_i] > arr[j]:
#                 min_i = j
#         arr[i], arr[min_i] = arr[min_i], arr[i]
#     return " ".join(map(str, arr))


# N = int(input())
# arr = list(map(int, input().split()))
# print(bubble_sort(N, arr))
# print(selection_sort(N, arr))