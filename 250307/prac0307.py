# 비트연산
'''
1bit: 0과 1을 표현하는 정보의 단위
1byte: 8bit
'''
arr = [1, 2, 3, 4, 5]
for i in range(1<<len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1<<idx):
            subset.append(arr[idx])
            total += arr[idx]
    if total == 10:
        print(f'부분집합: {subset}')

# 10726. 이진수 표현
'''
비트를 옆으로 한 칸씩 옮기며 1인지 물어보기
5
4 0
4 30
4 47
5 31
5 62
'''
# def solution():
#     target = M
#     for _ in range(N):  # 맨 우측 비트가 1인지 체크
#         if target & 0x1 == 0:
#             return False
#         target = target >> 1  # 맨 우측 비트 삭제

#     return True

def solution():
    # N개의 1을 구함
    mask = (1 << N) - 1
    result = (M&mask) == mask
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    result = solution()
