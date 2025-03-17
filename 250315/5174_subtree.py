import sys
sys.stdin = open('input5174.txt')


def preorder(n):
    if n == 0:
        return
    
    lst.append(n)
    preorder(left[n])
    preorder(right[n])
    return lst


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    parent = [0] * (E+2)
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p, c = edge[i*2], edge[i*2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parent[c] = p

    lst = []
    print(f'#{tc} {len(preorder(N))}')
