import sys
sys.stdin = open('input5176.txt')
'''
문제에 쓰인 번호 모양의 트리를 생성
해당 트리를 중위 순회로 읽은 다음
중위 순서의 인덱스 번호를 활용하여 답 도출
'''
# 트리를 읽을 중위 순회 함수 정의
def inorder(n):
    if n:
        inorder(left[n])
        arr.append(n)
        inorder(right[n])
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []

    # 문제에 주어진 번호가 노드에 저장된 값인 완전이진트리 생성
    edge = []
    for i in range(1, N+1):
        edge.append(i)
        edge.append(i*2)
        edge.append(i)
        edge.append(i*2+1)
        if i*2+1 == N:
            break

    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(N-1):
        p, c = edge[i*2], edge[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    arr = inorder(1)  # 루트 숫자는 언제나 1
    node = arr.index(N//2) + 1
    root = arr.index(1) + 1

    print(f'#{tc} {root} {node}')



