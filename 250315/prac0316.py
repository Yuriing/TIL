# def enq(n):
#     global last
#     last += 1
#     heap[last] = n

#     c = last
#     p = c // 2

#     while p and heap[p] > heap[c]:
#         heap[p], heap[c] = heap[c], heap[p]
#         c = p
#         p = c // 2

# N = int(input())
# last = 0
# heap = [0] * (N+1)

# arr = list(map(int, input().split()))

# for i in arr:
#     enq(i)

# print(heap)

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    heap = [0] * (N+1)
    for i in range(M):
        p, c = map(int, input().split())
        heap[p] = c

    for i in range(len(heap)-1, 1, -1):
        heap[i//2] += heap[i]

    print(f'#{tc} {heap[L]}')
