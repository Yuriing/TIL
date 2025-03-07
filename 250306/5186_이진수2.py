import sys
sys.stdin = open('input5186.txt')
'''
십진수의 소수점을 이진수로 변환하는 방법
1. 십진수의 소수점 i에 2를 곱한다.
2. 1을 넘길 경우 1을 뺀 값, 1을 넘기지 못할 경우 값 그대로에 2를 계속 곱한다.
3. 곱한 결과가 1이 되거나 반복적인 숫자가 나올 경우 종료한다.
4. 첫 곱셈 결과부터 정수부만 나열한 값이 해당 소수의 이진수이다.
'''
T = int(input())
for tc in range(1, T+1):
    N = float(input())

    bin_str = ''
    i = N
    while i < 1:
        if len(bin_str) > 12:
            print(f'#{tc} {"overflow"}')
            break

        if i*2 > 1:
            i = i*2 - 1
            bin_str = bin_str + '1'
        elif i*2 < 1:
            i = i*2
            bin_str = bin_str + '0'
        elif i*2 == 1:
            bin_str = bin_str + '1'
            print(f'#{tc} {bin_str}')
            break
