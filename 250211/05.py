import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = input()

    # 100*100 숫자 배열 리스트 생성
    int_Matrix = []
    for _ in range(100):
        int_Matrix.append(list(map(int, input().split())))

    # 방향 설정(하방, 우방, 우하방, 좌하방)
    dr = [1, 0, 1, 1]
    dc = [0, 1, 1, -1]

    # 합산 값을 넣을 빈 리스트 생성
    max_list = []
    
    r = 0
    c = 0
    for r in range(100):  # 열 방향 합산 값 계산
        num1 = 0
        for k in range(100):
            num1 += int_Matrix[r+dr[0]*k][c+dc[0]*k]
        max_list.append(num1)

    r = 0
    c = 0
    for c in range(100):  # 행 방향 합산 값 계산
        num2 = 0
        for k in range(100):
            num2 += int_Matrix[r+dr[1]*r][c+dc[1]*r]
        max_list.append(num2)

    num3 = 0
    for n in range(100):  # 오른쪽 대각선 방향 합산 값 계산
        num3 += int_Matrix[0+dr[2]*n][0+dc[2]*n]
    max_list.append(num3)

    num4 = 0
    for n in range(100):  # 왼쪽 대각선 방향 합산 값 계산
        num4 += int_Matrix[0+dr[3]*n][99+dc[3]*n]
    max_list.append(num4)

    print(f'#{tc} {max(max_list)}')