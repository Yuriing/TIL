import sys
sys.stdin = open('input1208.txt')

for T in range(1, 11):
    dump_num = int(input())
    box_arr = list(map(int, input().split()))

    n = 0
    while n < dump_num:
        box_arr[box_arr.index(max(box_arr))] = max(box_arr) - 1
        box_arr[box_arr.index(min(box_arr))] = min(box_arr) + 1
        n += 1

    result = max(box_arr) - min(box_arr)
    print(f'#{T} {result}')