import sys
sys.stdin = open('input2805.txt')


def thanksgiving(N, matrix):
    num1 = N//2
    harvest = 0
    for n in range(N//2):
        harvest = harvest + sum(matrix[n]) - sum(matrix[n][0:num1]) - sum(matrix[n][-1:-num1-1:-1])
        num1 -= 1
        if num1 == 0:
            break

    harvest += sum(matrix[N//2])

    num2 = 1
    for n in range(N//2+1, N):
        harvest = harvest + sum(matrix[n]) - sum(matrix[n][0:num2]) - sum(matrix[n][-1:-num2-1:-1])
        num2 += 1
        if num2 == 0:
            break

    return harvest


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().strip())))

    print(f'#{tc} {thanksgiving(N, matrix)}')