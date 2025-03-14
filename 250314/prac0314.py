'''
'''
'''
1861 정사각형 방
최악의 테케가 나오면 재귀호출로 풀었을 시 시간초과가 남
숫자들의 개수만큼 빈 공간이 있는 1차원 리스트를 저장해두고 연결된 곳이 있다면 1을 표시
연속된 1이 있는 수를 세면 얼마나 연결되어있는지를 알 수 있음
'''
# N*N visited 배열을 만든다
# 해당 숫자에서 갈 수 있다면 1을 기록한다
# 연속된 1의 길이가 가장 긴 곳이 정답이다
# 같은 길이가 있다면 더 작은 수가 정답

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * (N*N+1)

# 현재 위치 숫자 기준 상하좌우 확인
# 1 큰 곳이 있다면 visited 에 기록

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for y in range(N):
    for x in range(N):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위 밖으로 나가면 확인하지 않음
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if arr[ny][nx] == arr[y][x] + 1:
                visited[arr[y][x]] = 1
                break  # 나머지 델타 방향은 볼 필요 없다

# 연속된 1의 개수가 가장 긴 곳을 찾는다
# 가장 긴 곳, 현재 몇 개인지, 출발지
max_cnt = cnt = start = 0
for i in range(1, N*N+1):
    if visited[i] == 1:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
            start = i - cnt
        cnt = 0  # 개수 초기화

print(f'#1 {start} {max_cnt + 1}')

'''
1486 장훈이의 높은 선반
높이가 B 이상인 탑 중에서 가장 낮은 탑을 만드는 경우
해당 경우에서 B와 탑과의 높이 차를 구한다
'''
N, B = map(int, input().split())
heights = list(map(int, input().split()))
answer = float('inf')  # 장훈아!


def recur(cnt, total_height):
    """
    level: 점원 수
    branch: 탑에 포함시키거나 안 시키거나
    """
    global answer
    # 기저조건 가지치기
    if total_height >= B:  # 이미 B보다 큰 경우
        answer = min(answer, total_height)
        return

    if cnt == N:
        return

    recur(cnt+1, total_height + heights[cnt])  # 포함시키는 경우
    recur(cnt+1, total_height)  # 포함 안 시키는 경우


print(f'#1 {recur(N, 0)}')
'''
2819 격자판의 숫자 이어붙이기
격자를 움직이며 만든 7자리의 수를 중복 없이 세기
'''
# 시작지점: 다 봐야 한다
# 재귀를 돌리며 숫자를 붙인다
# 숫자가 7자리가 되면 set 에 넣는다(중복 제거)
matrix = [list(map(int, input().split())) for _ in range(4)]
result = set()


def recur2(y, x, number):
    if len(number) == 7:
        result.add(number)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        recur2(ny, nx, number+matrix[ny][nx])


for y in range(4):
    for x in range(4):
        recur2(y, x, 'matrix[y][x]')
'''
1952 수영장
level: 12월
branch: 4개
'''
# 완전탐색 버전
# 각 달의 4가지 케이스를 모두 확인하며 진행

# 이용권 가격들
cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
days = [0] + list(map(int, input().split()))  # 12개월어치 이용계획


def recur3(month, total_cost):
    global min_answer

    if min_answer < total_cost:  # 가지치기
        return

    if month > 12:
        min_answer = min(min_answer, total_cost)
        return

    # 1일권으로 다 사는 경우
    recur3(month+1, total_cost + (days[month]*cost_day))
    # 1달권으로 사는 경우
    recur3(month+1, total_cost + cost_month)
    # 3달권으로 사는 경우
    recur3(month+3, total_cost + cost_month3)
    # 1년 이용권으로 사는 경우
    recur3(month+12, total_cost + cost_year)


min_answer = float('inf')
recur3()

# DP 버전
# top-down 방식
# dp 에서는 메모이제이션이라고 부를 때가 많음
# 거듭제곱 문제

# bottom up 방식
# 시작점을 정해두고 앞으로 쌓아가면서 진행하는 방식(1, 2월)(3월부터 진행)
# 기존 값을 활용
# 가장 좋은 값을 계산해서 저장하며 나아감
# 점화식을 구하는 경우가 많음

# dp = [0] * 13
# # 시작점 초기화
# # 1월의 가격
# dp[1] = min
