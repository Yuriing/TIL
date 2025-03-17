import sys
sys.stdin = open('input1231.txt')


def inorder(n):
    if n == 0:
        return
    else:
        inorder(left[n])
        lst.append(n)
        inorder(right[n])
    
    return lst


for T in range(1, 11):
    N = int(input())

    alphabet_lst = [0] * (N+1)
    for i in range(N):
        node_lst = list(map(str, input().split()))
        alphabet_lst[int(node_lst[0])] = node_lst[1]

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
        p, c = edge[i*2], edge[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    
    lst = []
    inorder(1)

    alphabet = ''
    for i in lst:
        alphabet += alphabet_lst[i]
    
    print(f'#{T} {alphabet}')
