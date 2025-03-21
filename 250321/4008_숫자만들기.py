def dfs(cnt, total):
    global min_result, max_result

    if cnt == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    for i in range(4):
        if opers[i] == 0:
            continue

    opers[i] -= 1
    dfs(cnt+1, cal(total, numbers[cnt], i))


def cal(num1, num2, oper_idx):
    if oper_idx == 0:

    if oper_idx == 1:

    if oper_idx == 2:

    if oper_idx == 3:



N = int(input())
opers = list(map(int, input().split()))
numbers = list(map(int, input().split()))
min_result = float('-inf')
max_result = float('int')