import sys
sys.stdin = open('input1865.txt')
'''
r: 열 번호
prob: 지금까지 계산한 성공 확률
preempt: 앞선 직원이 선점한 일(set)
'''


def distribution(r, prob, preempt):
    global N, max_per

    if prob <= max_per:  # 가지치기. 지금까지 계산한 확률이 벌써 앞서 나온 성공 확률보다 작아졌을 경우
        return
    
    if r == N:  # 모든 직원이 일을 선택했을 경우
        max_per = max(max_per, prob)
        return
    
    for i in range(N):
        if i not in preempt:
            distribution(r+1, prob*matrix[r][i], preempt | {i})


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 정수에 미리 100을 나눠두고 함수에 적용
    for r in range(N):
        for c in range(N):
            matrix[r][c] = matrix[r][c] / 100
        
    max_per = 0
    distribution(0, 1, set())
    print(f'#{tc} {max_per*100:7f}')
