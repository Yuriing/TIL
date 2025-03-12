import sys
sys.stdin = open('input7456.txt')
'''
1부터 시작해서 1과 같은 무리에게 연락 돌리기(BFS 탐색)
1과 다른 무리면 visitied에 방문처리가 남지 않음.
방문처리가 안 된 사람 중 최소값부터 시작해서 그 사람과 같은 무리에게 연락 돌리기(BFS 탐색)
다른 무리면 아직 visited에 방문처리가 남지 않음.
방문처리가 안 된 사람 중 최소값부터 다시 시작
...
visited에 모두 방문처리가 될 때까지 반복
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        matrix[a][b] = 1
        matrix[b][a] = 1

    visited = [0]*(N+1)
    q = [1]  # 무조건 1로 시작
    visited[1] = 1  # 방문처리

    now = False  # 현재 상태
    k = 1  # 방문처리 숫자
    while now == False:
        while q:
            current = q.pop(0)

            for next in range(1, N+1):  # BFS로 current와 아는 사람 무리 탐색.
                if matrix[current][next] == 1 and visited[next] == 0:
                    q.append(next)
                    visited[next] = k

        for i in range(1, N+1):
            if visited[i] == 0:  # 연락 안 닿은 사람?
                q = [i]
                k += 1  # 다음 순번 무리
                visited[i] = k  # 방문처리
                break
        else:  # 다 연락 받았나요?
            now = True  # 첫번째 while문 종료
            break

    visited.pop(0)
    visited = set(visited)  # 방문처리 숫자 종류가 몇 개인지 도출

    print(f'#{tc} {len(visited)}')
