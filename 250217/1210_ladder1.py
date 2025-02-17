import sys
sys.stdin = open('input1210.txt')

for T in range(1, 11):
    tc = int(input())

    # 델타 설정(좌우)
    dr = [0, 0]
    dc = [-1, 1]

    ladder_matrix = []
    for _ in range(100):
        ladder_matrix.append(list(map(int, input().split())))

    for c in range(100):
        if ladder_matrix[99][c] == 2:
            start_c = c
            break

    r = 99
    c = start_c
    while r >= 0:
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 100 and 0 <= nc < 100 and ladder_matrix[nr][nc] == 1:
                ladder_matrix[r][c] = 0
                r = nr
                c = nc
            elif 0 <= nr < 100 and 0 <= nc < 100 and ladder_matrix[nr][nc] != 1 and ladder_matrix[r-1][c] == 1:
                r -= 1

        # else:
        #     r -= 1

    print(c)
