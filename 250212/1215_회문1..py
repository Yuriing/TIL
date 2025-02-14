import sys
sys.stdin = open('input3.txt')

for tc in range(1, 11):

    N = int(input())
    str_Matrix = []
    for _ in range(8):  # 문자열 세팅
        str_Matrix.append(list(input()))

    count = 0  # 회문의 개수 초기화
    for lst in str_Matrix:
        for idx in range(8-N+1):
            if lst[idx:idx+N] == lst[idx:idx+N][::-1]:
                count += 1

    for c in range(8):
        for r in range(8-N+1):
            for i in range(N // 2):
                left = r + i
                right = r + N - 1 - i
                if str_Matrix[left][c] != str_Matrix[right][c]:
                    break  # 회문이 아니면 중단
            else:
                count += 1  # 회문이면 카운트 증가

    print(f'#{tc} {count}')