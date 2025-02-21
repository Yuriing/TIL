from collections import deque
import sys
sys.stdin = open('input5099.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza_lst = deque(list(enumerate(map(int, input().split()), start=1)))

    oven = deque()
    for _ in range(N):
        oven.append(pizza_lst.popleft())

    while len(oven) > 1:
        pizza, cheese = oven.popleft()
        cheese = cheese // 2

        if cheese == 0:
            if pizza_lst:
                oven.append(pizza_lst.popleft())
        else:
            oven.append((pizza, cheese))

    print(f'#{tc} {oven[0][0]}')
