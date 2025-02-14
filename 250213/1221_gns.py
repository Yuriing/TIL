import sys
sys.stdin = open('input1221.txt')

T = int(input())
num_dict = {'ZRO': 0,
                'ONE': 1,
                'TWO': 2,
                'THR': 3,
                'FOR': 4,
                'FIV': 5,
                'SIX': 6,
                'SVN': 7,
                'EGT': 8,
                'NIN': 9,
                }
num_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(1, T+1):

    t_num, length = input().split()
    length = int(length)
    arr = input().split()

    for n in range(length):
        arr[n] = dict[arr[n]]

    arr.sort()

    for n in range(length):
        arr[n] = num_lst[arr[n]]

    print(f'{t_num} {"".join(arr)}')