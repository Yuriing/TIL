import sys
sys.stdin = open('input1240.txt')

password_lst = [
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

    password = []
    for r in range(N):
        for c in range(M-1, 0, -1):
            if matrix[r][c] == 1:
                password.extend(matrix[r][c-55:c+1])
                break
        if len(password) > 0:
            break

    lst = []
    for i in range(0, 56, 7):
        lst.append(password_lst.index(password[i:i+7]))
    
    print(f'#{tc}', end=" ")
    if (((lst[0] + lst[2] + lst[4] + lst[6])*3) + (lst[1] + lst[3] + lst[5] + lst[7])) % 10 == 0:
        print(sum(lst))
    else:
        print(0)
