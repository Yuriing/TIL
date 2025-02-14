import sys
sys.stdin = open('sample_input1.txt')

T = int(input())
for tc in range(1, T+1):

    str1, str2 = input(), input()
    N = len(str1)

    max_v = 0
    for i in range(N):
        count = 0
        for j in str2:
            if str1[i] == j:
                count += 1
            max_v = max(count, max_v)

    print(f'#{tc} {max_v}')