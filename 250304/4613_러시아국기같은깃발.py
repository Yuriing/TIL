import sys
sys.stdin = open('input4613.txt')


# 색깔 중복조합 뽑는 함수
def repetition(data, N):
    result = []

    def dfs(path):
        if len(path) == N:
            result.append(path)

        for i in range(len(data)):
            dfs(path+data[i])

    dfs([])
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = []
    for _ in range(N):
        flag.append(list(map(str, input().strip())))

    count1 = 0
    # 첫째줄을 흰색으로 밀어버리기
    for color in flag[0]:
        if color != 'W':
            count1 += 1

    # 마지막줄을 빨강으로 밀어버리기
    for color in flag[N-1]:
        if color != 'R':
            count1 += 1

    # 할 수 있는 색깔 조합 다 생각해내기
    data = ['B', 'R', 'W']
    palette = list(repetition(data, N-2))

    r = 1
    count2 = 0
    lst = []
    while r < N-1:

        for color in flag[r]:
            if color != palette[r-1]:
                count2 += 1

        lst.append(count2)
        r += 1