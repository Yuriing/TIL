import sys
sys.stdin = open('input5189.txt')

# 들를 관리구역 번호와 그에 따른 배터리 소모량의 최소값을 구하는 함수
def perm(selected, remain, current):
    global min_battery
    # 만일 현재 배터리 소모량이 이미 현재의 최소 배터리 소모량을 넘어섰을 경우 현재 경로 탐색을 종료한다
    if current > min_battery:
        return

    if not remain:  # 관리구역을 다 돌았을 때 사무실로 돌아오게 한다
        current += matrix[selected[-1]-1][0]
        min_battery = min(current, min_battery)
        return

    for i in range(len(remain)):  # 들르게 되는 관리구역에 따라 배터리 소모량을 측정한다
        pick = remain[i]
        new_remain = remain[:i] + remain[i+1:]
        perm(selected+[pick], new_remain, current+matrix[selected[-1]-1][pick-1])


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 2부터 N까지의 자연수를 모두 뽑아 num 리스트 생성
    num = [i for i in range(2, N+1)]
    min_battery = float('inf')

    perm([1], num, 0)

    print(f'#{tc} {min_battery}')
