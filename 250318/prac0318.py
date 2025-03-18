# 4 * 4 N-Queen 문제
# (y, x) 좌표에 queen 을 놓은 적이 있다
# visited 기록 방법
#   이차원 배열
#   일차원 배열로 효율적으로 하는 방법
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[i][col]:
            return False
    # 2. 왼쪽 대각선
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False

        i -= 1
        j -= 1

    # 3. 오른쪽 대각선
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False

        i -= 1
        j += 1

    return True


def dfs(row):
    global answer
    if row == N:  # N개의 행에 놓았다
        answer += 1
        return

    # N개의 열에 대해 고려해야함
    for col in range(N):
        if check(row, col):
            visited[row][col] = 1
            dfs(row + 1)
            visited[row][col] = 0


N = 8
visited = [[0] * N for _ in range(N)]
answer = 0

dfs(0)
print(answer)
