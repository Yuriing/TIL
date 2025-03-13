import sys
sys.stdin = open('input5201.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    weight.sort()
    truck.sort()

    total_weight = 0
    while weight:
        w = weight.pop()

        if len(truck) == 0:
            break

        if w > truck[-1]:
            continue
        else:
            total_weight += w
            truck.pop()

    print(f'#{tc} {total_weight}')
