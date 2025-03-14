import sys
sys.stdin = open('input1952.txt')


def recur3(month, total_cost):
    global min_answer

    if min_answer < total_cost:  # 가지치기
        return

    if month > 12:
        min_answer = min(min_answer, total_cost)
        return

    # 1일권으로 다 사는 경우
    recur3(month+1, total_cost + (days[month]*cost[0]))
    # 1달권으로 사는 경우
    recur3(month+1, total_cost + cost[1])
    # 3달권으로 사는 경우
    recur3(month+3, total_cost + cost[2])
    # 1년 이용권으로 사는 경우
    recur3(month+12, total_cost + cost[3])


T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    # cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    days = [0] + list(map(int, input().split()))  # 12개월어치 이용계획

    min_answer = float('inf')
    recur3(0, 0)
    print(f'#{tc} {min_answer}')
