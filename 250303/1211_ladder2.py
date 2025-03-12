import sys
sys.stdin = open('input1211.txt')

for _ in range(1, 11):
    T = int(input())

    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    # 좌, 우, 하
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    count = 0
    max_v = 300
    answer_j = 0
    for j in range(100):
        if matrix[0][j] == 1:
            r, c = 0, j
            visited = [row[:] for row in matrix]
            visited[0][j] = 3

            while r < 99:
                for i in range(3):
                    if 0 <= r+dr[i] < 100 and 0 <= c+dc[i] < 100:
                        nr = r + dr[i]
                        nc = c + dc[i]

                        if matrix[nr][nc] == 1:
                            visited[nr][nc] = 3
                            count += 1
                            r = nr
                            c = nc
                            break
                        else:
                            continue
            
            if max_v <= count:
                max_v = count
                answer_j = j


    print(f'#{T} {answer_j}')

# for _ in range(1, 11):
#     T = int(input())

#     matrix = []
#     for _ in range(100):
#         matrix.append(list(map(int, input().split())))

#     min_distance = 300
#     answer_j = 0

#     for j in range(100):
#         if matrix[0][j] == 1:
#             r, c = 0, j
#             distance = 1
#             matrix[r][c] = distance  # 방문 처리 및 거리 누적

#             while r < 99:
#                 # 왼쪽으로 계속
#                 if c > 0 and matrix[r][c - 1] == 1:
#                     while c > 0 and matrix[r][c - 1] == 1:
#                         c -= 1
#                         distance += 1
#                         matrix[r][c] = distance

#                 # 오른쪽으로 계속
#                 elif c < 99 and matrix[r][c + 1] == 1:
#                     while c < 99 and matrix[r][c + 1] == 1:
#                         c += 1
#                         distance += 1
#                         matrix[r][c] = distance

#                 # 아래로 이동
#                 r += 1
#                 distance += 1
#                 matrix[r][c] = distance

#             # 마지막 줄(r == 99)에 도착했을 때 거리 확인
#             if distance <= min_distance:
#                 min_distance = distance
#                 answer_j = j


#     print(f'#{T} {answer_j}')

# for _ in range(1, 11):
#     T = int(input())

#     matrix = []
#     for _ in range(100):
#         matrix.append(list(map(int, input().split())))

#     min_distance = float('inf')
#     answer_j = 0

#     for j in range(100):
#         if matrix[0][j] == 1:
#             r, c = 0, j
#             visited = [row[:] for row in matrix]  # matrix 원본 유지용 복사본
#             visited[r][c] = 2  # 방문 처리
#             distance = 1

#             while r < 99:
#                 # 왼쪽으로 이동할 수 있으면 계속 이동
#                 if c > 0 and visited[r][c - 1] == 1:
#                     while c > 0 and visited[r][c - 1] == 1:
#                         c -= 1
#                         distance += 1
#                         visited[r][c] = 2

#                 # 오른쪽으로 이동할 수 있으면 계속 이동
#                 elif c < 99 and visited[r][c + 1] == 1:
#                     while c < 99 and visited[r][c + 1] == 1:
#                         c += 1
#                         distance += 1
#                         visited[r][c] = 2

#                 # 좌우가 막히면 아래로 이동
#                 r += 1
#                 distance += 1
#                 visited[r][c] = 2

#             # 최단 거리 갱신
#             if distance < min_distance:
#                 min_distance = distance
#                 answer_j = j

#     print(f'#{T} {answer_j}')