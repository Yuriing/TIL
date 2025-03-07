import sys
sys.stdin = open('input1240.txt')

password = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],
]

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().strip())))

    r = 0
    c = 0
    code = []
    for r in range(N):
        for c in range(M-1, 0, -1):
            if matrix[r][c] == 1:
                code.extend(matrix[r][c-55:c+1])
                break
        if len(code) > 0:
            break

    dec_num = []
    for i in range(0, 56, 7):
        for num in password:
            if code[i:i+7] == num:
                dec_num.append(password.index(num))

    if ((dec_num[0]+dec_num[2]+dec_num[4]+dec_num[6])*3 + (dec_num[1]+dec_num[3]+dec_num[5]+dec_num[7])) % 10 == 0:
        print(f'#{tc} {sum(dec_num)}')
    else:
        print(f'#{tc} {0}')

