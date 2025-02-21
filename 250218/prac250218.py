v = 7
E = 8
data = list(map(int, input().split()))

adj_matrix = [[0]*(v+1) for _ in range(v+1)]

for i in range(E):
    n1, n2 = data[i*2], data[i*2+1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

for row in adj_matrix:
    print(row)

'''
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
인접행렬:
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 1, 1, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 1]
[0, 0, 1, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 1, 1, 0, 1]
[0, 0, 0, 1, 0, 0, 1, 0]
'''
# 여기까지가 기초 다지기


def DFS_stack(start):
    '''
    start: 시작노드 번호
    visited: 방문 여부 확인용 체크리스트
    '''
    stack = [start]  # 시작 노드 삽입한 상태로 스택 초기화
    visited = [0] * (v+1)
    while stack:  # 스택이 비어있지 않을 동안
        current_node = stack.pop()  # 시작 노드 뽑기

        if visited[current_node] == 0:  # 간 적 없다
            visited[current_node] = 1  # 방문 처리
            print(current_node, end='')  # 방문한 노드 출력(줄바꿈 없이)

            for next_node in range(v, 0, -1):
                '''
                v~1 역순 확인
                작은 번호를 마지막에 확인함으로써 작은 번호가 스택 위쪽에 위치하게
                현재 갈래길에서 오름차순으로 길을 선택하기 때문. 만약 내림차순이라면 작은 번호 우선 확인
                '''
                if adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                    # 현재 노드에서 길이 뚫려있고
                    # 길이 뚫린 곳 중 안 간 노드
                    stack.append(next_node)


DFS_stack(1)