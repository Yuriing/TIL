T = int(input())
for tc in range(1, T+1):
    N, hex_num = map(str, input().split())
    N = int(N)

    bin_num = ''
    for i in range(N):
        bin_num += format(int(hex_num[i], 16), '04b')

    print(f'#{tc} {bin_num}')
