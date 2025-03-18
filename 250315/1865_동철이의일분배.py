import sys
sys.stdin = open('input1865.txt')


def distribution(r, prob, preempt):
    global N, max_per

    if r == N:
        max_per = max(max_per, prob)
        return
    
    if prob < max_per:
        return
    
    for i in range(N):
        if i not in preempt:
            distribution(r+1, prob*(matrix[r][i]/100), preempt + [i])


T = int(input())
for tc in range(1, T):
    N = int(input())
    
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
        
    max_per = 0
    distribution(0, 1, [])
    result = round(max_per*100, 6)
    print(f'#{tc} {result}')
