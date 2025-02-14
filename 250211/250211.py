# # 01
# ## 뒤집은 문자열을 for 문으로 하나씩 검사한 뒤 결과 출력
# txt1 = input()
# txt2 = txt1[::-1]
# N = int(len(txt1))

# for idx in range(N):
#     if txt1[idx] != txt2[idx]:
#         print('0')
#         break
# else:
#     print('1')


# ## 문자열 가운데를 기준으로 양쪽의 문자 비교
# txt3 = input()
# N = int(len(txt3))

# for idx in range(N//2):
#     if txt3[idx] == txt3[N-1-idx]:
#         print('1')
#         break
# else:
#     print('0')


# # 02 회문
# '''
# N: 한 줄 당 글자 수
# M: 찾아야할 회문의 글자 수
# '''
# # 문자열을 N*N 크기의 이차원 배열로 전환
# N, M = map(int, input().split())

# str_matrix = []
# for _ in range(N):
#     str_matrix.append(list(input()))

# # 우방향 검사
# for line in str_matrix:
#     for i in range(N):
#         if line[i] == line[N-1-i]:
#             print(''.join(line))
#             break

# else:  # 하방향 검사
#     for r in range(N):
#         for c in range(N):
#             if r < c:
#                 str_matrix[r][c], str_matrix[c][r] = str_matrix[c][r], str_matrix[r][c]
    
#     for line in str_matrix:
#         for i in range(N):
#             if line[i] == line[N-1-i]:
#                 print(''.join(line))
#                 break

# # 03 파리퇴치
# '''
# N: 주어지는 숫자 배열의 가로세로 값
# M: 파리채 영역의 가로세로 값
# '''
# N, M = map(int, input().split())

# # N*N 배열의 숫자 2차원 리스트 생성
# int_matrix = []
# for _ in range(N):
#     int_matrix.append(list(map(int, input().split())))

# # 죽은 파리 마리수를 담을 빈 리스트 생성
# bug_count = []

# # N*N 배열 안을 돌며 나올 수 있는 죽은 파리 마리수의 경우의 수를 전부 구함
# for r in range(N-M+1):
#     for c in range(N-M+1):
#         sum = int(int_matrix[r][c]) + int(int_matrix[r][c+1]) + int(int_matrix[r+1][c]) + int(int_matrix[r+1][c+1])
#         bug_count.append(sum)

# # 리스트 내 최대값 프린트
# print(max(bug_count))


# 04 풍선팡!
'''
N: 행 개수
M: 열 개수
'''
N, M = map(int, input().split())

# N*M 형태의 이차원 배열 생성
int_matrix = []
for _ in range(N):
    int_matrix.append(list(map(int, input().split())))

# 자리마다 돌면서 해당 자리의 풍선이 터질 시 날리는 꽃가루의 개수를 합산
# 합산한 결과를 max_list에 넣음
max_list = []
for r in range(N):
    for c in range(M):
        num = int_matrix[r][c]
        int_sum = 0
        for n in range(1, num+1):
            # n을 더하거나 뺀 값이 리스트 범위를 벗어날 경우 합산하지 않음
            if 0 <= r + n < N:
                int_sum += int_matrix[r+n][c]
            if 0 <= r - n < N:
                int_sum += int_matrix[r-n][c]
            if 0 <= c + n < M:
                int_sum += int_matrix[r][c+n]
            if 0 <= c - n < M:
                int_sum += int_matrix[r][c-n]
        max_list.append(num+int_sum)



print(max(max_list))