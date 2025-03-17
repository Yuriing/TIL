import sys
sys.stdin = open('input5176.txt')


def inorder(n):
    if n != 0:
        inorder(left[n])
        lst.append(n)
        inorder(right[n])
    return lst


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    edge = []
    i = 1
    while True:
        edge.append(i)
        edge.append(i*2)
        if i*2 == N:
            break

        edge.append(i)
        edge.append(i*2 + 1)
        if i*2 + 1 == N:
            break

        i += 1

    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N-1):
        p, c = edge[i*2], edge[i*2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    lst = []
    inorder(1)
    root = lst.index(1) + 1
    node = lst.index(N//2) + 1

    print(f'#{tc} {root} {node}')
