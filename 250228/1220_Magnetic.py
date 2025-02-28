import sys
sys.stdin = open('input1220.txt')

for tc in range(1, 11):
    T = int(input())

    matrix = []
    for _ in range(T):
        matrix.append(list(map(int, input().split())))

    stack = []
    c = 0
    count = 0
    while c < 100:
        for r in range(T):
            if len(stack) > 0 and matrix[r][c] > 0 and stack[len(stack)-1] != matrix[r][c]:
                stack.append(matrix[r][c])

            elif len(stack) == 0 and matrix[r][c] == 1:
                stack.append(matrix[r][c])

        count += (len(stack)//2)
        c += 1
        stack.clear()

    print(f'#{tc} {count}')