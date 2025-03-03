import sys
sys.stdin = open('input1226.txt')

import copy

def mazerun(maze):
    
    maze_visited = copy.deepcopy(maze)  # 원래 미로 리스트를 그대로 받아 방문처리 리스트로 사용

    q = []
    r, c = 1, 1
    q.append((r, c))  # 좌표값을 튜플로 묶어 큐에 삽입
    maze_visited[r][c] = 5

    # 좌 우 상 하
    # 예제 문제를 보니 좌우로 먼저 움직이는 게 효율적일 듯 해서...
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        # 현재 위치 pop
        r, c = q.pop(0)
        current = maze[r][c]

        for i in range(4):  # 다음 위치 탐색
            if 0 <= r+dr[i] < 16 and 0 <= c+dc[i] < 16:
                nr = r + dr[i]
                nc = c + dc[i]

                # 탐색한 곳이 갈 수 있는 위치이고 아직 방문하지 않은 위치라면
                if maze[nr][nc] == 0 and maze_visited[nr][nc] == 0:
                    q.append((nr, nc))  # 큐에 튜플 형식으로 삽입
                    maze_visited[nr][nc] = 5  # 방문 처리. 다른 숫자와 헷갈리지 않게끔 다른 숫자 지정
                if maze[nr][nc] == 3:  # 만약 3을 찾았다면 바로 반복문 종료
                    return 1
                
    # 3을 찾지 못하고 while문이 종료되었을 경우
    return 0


for _ in range(1, 11):
    T = int(input())

    maze = []
    for _ in range(16):
        maze.append(list(map(int, input().strip())))

    result = mazerun(maze)

    print(f'#{T} {result}')
