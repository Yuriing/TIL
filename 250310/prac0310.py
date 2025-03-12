# 20551 증가하는 사탕수열
# 문제 읽기
## 두번째 상자는 세 번째 상자보다 작게
## 첫번째 상자는 두 번째 상자보다 작게
### ----- ###
# 설계
## 자료구조
## 3개의 숫자 + 먹은 갯수만 저장(변수 4개)
## 리스트 / A, B, C 3개 정도면 변수로 저장해도 ok

# 알고리즘
## B는 C보다 작아야 한다
# (사탕의 개수가 많으면 시간 초과 가능성)
## B가 C보다 크거나 같다면 B = C -1 로 만들어준다

# 기타사항
## B는 2 이상
## C는 3 이상
### ----- ###
T = int(input())
for tc in range(1, T+1):
    # 변수가 3개만 있기 때문에 리스트로 받지 않음
    A, B, C = map(int, input().split())

    # 불가능한 케이스 제거
    if B < 2 or C < 3:  # A < B < C 구조를 못 만드는 경우
        print(f'#{tc} -1')
        continue  # 이 문제는 끝났으니 다음 테스트 케이스를 봐라

    eatcount = 0
    # B >= C라면, B = C-1로 만들자
    if B >= C:
        eatcount += B - (C-1)
        B = C - 1

    # A >= B라면, A = B-1로 만들자
    if A >= B:
        eatcount += A - (B-1)
        A = B - 1

    print(f'#{tc} {eatcount}')

# 10580 전봇대
# 문제 읽기
## 전선 N개
## 교차점이 발생. 해당 교차점의 개수를 count
### ----- ###
# 설계
## 교차점은 무슨 조건일 때 발생할까?
## 새로운 선의 시작점이 기존 선의 시작점보다 높고 and 새로운 선의 도착점이 기존 선의 도착점보다 낮은 경우
## 새로운 선의 시작점이 기존 선의 시작점보다 낮고 and 새로운 선의 도착점이 기존 선의 도착점보다 높은 경우
### 기존 선들을 저장하면서 진행
### 새로운 선을 추가할 때마다 비교를 진행
### (시간적으로 매우 여유로운 문제)
### ----- ###
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 선의 개수
    
    # 새로운 선을 추가하며 비교를 진행
    # 기존 선들과 비교
    wires = []  # 기존 선들을 저장할 리스트
    answercount = 0  # 교차점 개수

    for n in range(N):
        start, end = map(int, input().split())

        # 기존 선들과 비교
        for prev_start, prev_end in wires:
            # 교차점 조건1. 기존의 전선보다 시작점이 높고 도착점이 낮음
            if start > prev_start and end < prev_end:
                answercount += 1
            # 교차점 조건2. 기존의 전선보다 시작점이 낮고 도착점이 높음
            if start < prev_start and end < prev_end:
                answercount += 1

        # 비교 후 목록에 전선 추가
        wires.append((start, end))

    print(f'#{tc} {answercount}')

# 1953 탈주범 검거
# 문제 읽기
## 지도는 이차원 배열
## 맨홀 뚜껑 위치가 정해짐
## 맨홀 뚜껑을 기준으로 넓어지는 그림
## 이동할 수 있는 개수를 구해라
## 이동 방향(상하좌우)/이동 못 하는 경우
### ----- ###
# 설계
## 이차원 리스트 형태 + 미로 탐색 문제 유형
## DFS, BFS
## 주변으로 퍼져나가면서 확인하자(BFS)
## 방문체크
## 시간 누적하면서 +1씩 진행

# 알고리즘
## BFS 시간복잡도: O(V+E)
## 큐를 활용하여 먼저 방문한 노드부터 탐색을 시작
## 먼저 방문한 노드에서 갈 수 있는 노드들을 후보군에 추가
### ----- ###
# 이동: 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 이동이 불가능한 케이스
## 범위 밖으로 나갔을 때
## 이미 방문한 곳은 안 감
## 현재 내 위치에서 뚫려있지 않은 곳
## 가려는 곳에 터널이 뚫려있지 않은 곳

# 터널의 종류에 따라 이동 가능 여부를 기록
types = {
    1: [1, 1, 1, 1], 
    2: [1, 1, 0, 0], 
    3: [0, 0, 1, 1], 
    4: [1, 0, 0, 1], 
    5: [0, 1, 0, 1], 
    6: [0, 1, 1, 0], 
    7: [1, 0, 1, 0], 
}

from collections import deque

# 리스트의 제일 앞에서 요소를 꺼내면 리스트의 길이만큼 시간 발생

def bfs(R, C):
    dq = deque([(R, C)])
    visited[R][C] = 1  # 출발점 초기화

    while dq:
        nowy, nowx =  dq.popleft()
        dirs = types[graph[nowy][nowx]]

        for i in range(4):
            if dirs[i] == 0:
                continue

            new_y = nowy + dy[i]
            new_x = nowx + dx[i]

            # 범위 밖으로 넘어가면 pass
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            # 이미 방문했으면 pass
            if visited[new_y][new_x] == 0:
                continue

            # 못 가면 pass
            next_dirs = types[graph[new_y][new_x]]

            # next_dirs가 안 뚫려있으면 못 감
            if i % 2 == 0 and next_dirs[i+1] == 0:
                continue

            if i % 2 == 1 and next_dirs[i-1] == 0:
                continue

            visited[new_y][new_x] = visited[nowy][nowx] + 1
            dq.append((new_y, new_x))


T = int(input())
for tc in range(1, T+1):
    # BFS로 접근
    # 방문기록을 해야 한다
    N, M, R, C, L = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]  # 특정 좌표까지 몇 시간이 걸렸는지 기록할 예정

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

# 5656 벽돌 깨기
# 문제 읽기
## 시뮬레이션
## 경우의 수를 다 봐야 한다 > DFS
## 재귀호출로 벽돌이 깨진 상태를 다시 불러오기
## 구슬을 모두 발사 or 남은 벽돌이 0이면 재귀호출 종료

# 알고리즘
## 떨구기 전 상태를 깊은복사
## 복사한 리스트에 구슬 떨구기
## cnt+1번 상태로 이동(다음 재귀 호출)
## 떨구기 전 상태로 복구

## 떨구기 전 상태를 복사
## 복사한 리스트에 구슬 떨구기
## cnt+1번 상태로 이동 + 떨군 상태를 함께 전달(다음 재귀 호출)