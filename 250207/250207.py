# # 01 연습문제1_Delta
# matrix_a = [list(map(int, input().split())) for _ in range(5)]

# # 상하좌우 델타 값 생성
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# # 전체 합을 저장할 변수
# total_sum = 0

# # 상하좌우 값을 list_a에 넣는다
# for r in range(5):
#     for c in range(5):
#         list_a = []
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < 5 and 0 <= nc < 5:
#                 list_a.append(matrix_a[nr][nc])

#         '''
#         matrix_a[r][c]의 값을 list_a의 길이만큼 복사하여 새 리스트를 만든다.
#         벽에 접해있는 원소는 list_a에 원소가 4개 미만으로 담기므로 리스트 길이를 추출한다
#         '''

#         list_b = [matrix_a[r][c]] * len(list_a)

#         new_matrix = [list_a, list_b]

#         '''
#         new_matrix = [
#             [7, 7, 7, 7],
#             [2, 12, 6, 8],
#             ]
#         '''
#         list_c = list(map(list, zip(*new_matrix)))
#         '''
#         list_c = [
#                     [7, 2],
#                     [7, 12],
#                     [7, 6],
#                     [7, 8],
#                     ]
#         '''
#         # 절댓값 계산
#         for item in list_c:
#             if item[0] >= item[1]:
#                 total_sum = total_sum + item[0] - item[1]
#             else:
#                 total_sum = total_sum + item[1] - item[0]

# # 결과 출력
# print(total_sum)


# # 02 연습문제2_subset
# arr = list(map(int, input().split()))

# for i in range(1 << 10):  # 2^10개의 부분집합 도출
#     result = 0
#     for j in range(10):  # i의 자리수 10
#         if i == 1<<j:  # i가 1이 j 자리에 있는 수일 때
#             result += arr[j]  # 부분집합의 합을 result에 추가

#     if result == 0:  # 부분집합의 합 중 0이 되는 게 있을 때
#         print(True)
#         break  # 반복 중단

# else:  # 한 번만 출력되도록 반복문에서 벗어난 위치에 작성
#     print(False)


# 03 색칠하기
# (0, 0)부터 (9, 9)까지 있는 좌표 생성
empty_list = [[0] * 10 for _ in range(10)]

N = int(input())
list_color = [[0] * 5 for _ in range(N)]

lists = []
for n in range(N):
    lists.append(list(map(int, input().split())))

color_coor = []
for lst in lists:
    color_coor.append([lst[0], lst[1]])
    color_coor.append([lst[2], lst[3]])

# empty_list에서 [1, 2]부터 [1, 3]까지
# [2, 2]부터 [2, 3]까지
# [3, 2]부터 [3, 3]까지
for coor in color_coor:
    empty_list[coor[0]][coor[1]] = 1