import sys
sys.stdin = open('input1221.txt')

GNS = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for _ in range(T):
    tc, num = map(str, input().split())
    num = int(num)

    lst = list(map(str, input().split()))

    for n in range(num):
        if lst[n] == GNS[GNS.index(lst[n])]:
            lst[n] = GNS.index(lst[n])

    lst.sort()

    for n in range(num):
        lst[n] = GNS[lst[n]]

    print(f'{tc} {" ".join(map(str,lst))}')
