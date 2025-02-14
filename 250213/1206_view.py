import sys
sys.stdin = open('input1206.txt')

for T in range(1, 11):
    num = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for n in range(2, num-2):
        lst = [arr[n-2], arr[n-1], arr[n], arr[n+1], arr[n+2]]
        lst.sort()
        if lst[-1] == arr[n]:
            count += (arr[n] - lst[-2])

    print(f'#{T} {count}')
