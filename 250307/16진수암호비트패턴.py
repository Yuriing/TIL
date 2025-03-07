'''
2
0DEC
0269FAC9A0
'''

# 인덱스 넘버를 이용하여 암호를 받음
pattern = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '110111',
    '001011',
    '111101',
    '011001',
    '101111',
]

T = int(input())
for tc in range(1, T+1):
    N = input()  # 16진수 배열 받기

    d_num = ''
    for num in N:  # 16진수 배열을 2진수 배열로 바꾸기
        number = int(num, 16)
        d_num += format(number, '04b')

    M = len(d_num)
    i = M-1  # 2진수 배열을 뒤에서부터 검사
    lst = []
    while i > 0:
        if d_num[i] == '1':  # 1을 찾으면 6자리를 슬라이스하여 해독
            lst.append(pattern.index(d_num[i-5:i+1]))
            i -= 6  # i 갱신
        else:  # 1을 찾지 못하면 계속 검사
            i -= 1

    # 뒤에서부터 받았기 때문에 순서가 뒤바뀌어있음. 순서 교체
    lst.reverse()

    print(f'#{tc} {" ".join(map(str, lst))}')
