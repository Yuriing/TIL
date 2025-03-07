'''
2
0F97A3
01D06079861D79F99F
'''

T = int(input())
for tc in range(1, T+1):
    hex_str = input()  # 16진수를 str 형태로 받음

    # 10진수로 변환 후 2진수로 변환
    dec_str = ''
    for i in hex_str:
        num = int(i, 16)
        dec_str = dec_str + format(num, '04b')

    # 번호 먼저 프린트
    print(f'#{tc}', end=" ")
    i = 0
    while i < len(dec_str):
        bin_str = ''
        # 7개의 숫자가 전부 0일 때 앞 4비트 버리기
        if dec_str[i:i+7] == '0000000':
            i = i + 4

        if i+7 < len(dec_str):
            bin_str += dec_str[i:i+7]
        else:
            bin_str += dec_str[i::]

        i += 7

        print(int(bin_str, 2), end=" ")
