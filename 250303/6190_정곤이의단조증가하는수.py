import sys
sys.stdin = open('input6190.txt')

import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    arr_lst = []
    for i in range(1, 1<<N):
        arr = []
        for j in range(N):
            if i & (1<<j):
                arr.append(lst[j])
        if len(arr) == 2:
            arr_lst.append(arr)

    multiple = []
    for nums in arr_lst:
        result = math.prod(nums)
        multiple.append(result)

    monotone = []
    for i in multiple:
        if i >= 10:
            str_num = str(i)
            for j in range(len(str_num)-1):
                if str_num[j] > str_num[j+1]:
                    break
            else:
                i = int(i)
                monotone.append(i)

    if len(monotone) == 0:
        value = -1
    else:
        value = max(monotone)


    print(f'#{tc} {value}')
