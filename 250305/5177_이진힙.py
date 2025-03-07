import sys
sys.stdin = open('input5177.txt')

def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c // 2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)
    last = 0

    arr = list(map(int, input().split()))

    for i in arr:
        enq(i)

    i = N//2
    plus = 0
    while i >= 1:
        plus += heap[i]
        i = i//2

    print(f'#{tc} {plus}')
