# 03 숫자카드
import sys
sys.stdin = open('input4834.txt')

'''
카드에 적힌 숫자의 범위는 0<=a<=9
인덱스 번호가 0부터 9까지 모두 생성되도록 구간 10개 생성
'''

def max_card(arr):
    arr_list = [0] * 10
    for num in arr:  # 숫자 a가 있을 시 인덱스 번호 a에 해당하는 구간 +1
        arr_list[num] += 1

    max_count = max(arr_list)

    for i in range(9, -1, -1):
        if arr_list[i] == max_count:
            return i, max_count



T = int(input())  # 번호 생성
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, str(input())))  # 카드 배열

    print(f'#{tc} {" ".join(map(str, max_card(arr)))}')