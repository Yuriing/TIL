import sys
sys.stdin = open('input4.txt')


for tc in range(1, 11):
    T = int(input())
    str_Matrix = []
    for _ in range(100):
        str_Matrix.append(list(input()))

    max_v = []

    for lst in str_Matrix:
        for i in range(100):
            for n in range(100-i):
                # if i+n < 99:
                if lst[i:i+n] == lst[i:i+n][::-1]:
                    max_v.append(n)

    # str_Matrix 의 위아래를 바꾸기
    for r in range(100):
        for c in range(100):
            if r < c:
                str_Matrix[r][c], str_Matrix[c][r] = str_Matrix[c][r], str_Matrix[r][c]

    for lst in str_Matrix:
        for i in range(100):
            for n in range(100-i):
                # if i + n < 99:
                if lst[i:i + n] == lst[i:i + n][::-1]:
                    max_v.append(n)

    print(f'#{T} {max(max_v)}')