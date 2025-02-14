import sys
sys.stdin = open('sample_input2.txt')

T = int(input())
for tc in range(1, T+1):
    str1, str2 = input(), input()

    N = len(str1)  # XYPV
    M = len(str2)  # EOGGXYPVSY

    i = 0
    j = 0  # str1, str2의 인덱스 값 초기화

    while i < N and j < M:
        if str1[i] != str2[j]:
            i = 0
            j -= (i - 1)
        else:
            i += 1
            j += 1
    if i == N:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
