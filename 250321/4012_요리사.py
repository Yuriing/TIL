'''
'''
'''
뭐가 더 좋을 지 알 수 없음
모두 넣어보는 완전탐색으로 가야 함

재료를 하나씩 선택하면서 A에 넣는다
위 과정을 재료 수의 반을 선택할 때까지 반복한다
반을 선택한 후 A요리와 B요리 시너지의 차이를 계산한다
'''


def cal_synergy(lst):

    total = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            total += matrix[lst[i]][lst[j]] + matrix[lst[j]][lst[i]]

    return total



def get_synergy():
    A_list, B_list = [], []
    for i in range[N]:
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)


def dfs(cnt, a_cnt):
    global answer

    if cnt == N // 2:
        a_total, b_total = get_synergy()
        answer = min(answer, abs(a_total - b_total))
        return

    for food_num in range(a_cnt, N):
        if visited[food_num]:
            continue

        visited[food_num] = 1
        dfs(cnt+1, food_num+1)
        visited[food_num] = 0


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N  # 특정 재료 사용 여부
answer = float('inf')