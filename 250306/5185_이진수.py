import sys
sys.stdin = open('input5185.txt', 'r')

# 내장함수 사용
# T = int(input())
# for tc in range(1, T+1):
#     N, hex_str = map(str, input().split())
#     N = int(N)
#
#     bin_str = ''
#     for i in range(N):
#         dec_num = int(hex_str[i], 16)
#         bin_str += format(dec_num, '04b')
#
#     print(f'#{tc} {bin_str}')

# 내장함수 미사용
T = int(input())
for tc in range(1, T+1):
    N, hex_str = map(str, input().split())
    N = int(N)

    hex_num = '0123456789ABCDEF'

    dec_num2 = 0
    bin_num2 = ''
    for i in range(N):
        idx = hex_num.index(hex_str[i])
        dec_num2 += idx

        while dec_num2 > 0:
            bin_num2 = bin_num2 + str(dec_num2 % 2)
            dec_num2 //= 2

    print(f'#{tc} {dec_num2}')
