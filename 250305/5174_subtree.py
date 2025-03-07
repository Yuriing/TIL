import sys
sys.stdin = open('input5174.txt')

def preorder(n):
    if n == 0:
        return
    lst.append(n)
    preorder(tree[n][0])
    preorder(tree[n][1])
    return lst


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    lst = []

    tree = [[0]*3 for _ in range(E+2)]

    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    print(f'#{tc} {len(preorder(N))}')
