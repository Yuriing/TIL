import sys
sys.stdin = open('input5248.txt')


def find_set(x):  # 대표자 찾기
    if representative[x] == x:
        return x

    representative[x] = find_set(representative[x])

    return representative[x]


def union(x, y):  # 작은 수를 대표자로 하여 해당 집합에 병합
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x != ref_y:
        if ref_x < ref_y:
            representative[ref_y] = ref_x
        else:
            representative[ref_x] = ref_y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    representative = [i for i in range(N+1)]  # 자기 자신을 대표자로 하여 초기 조 편성

    arr = list(map(int, input().split()))
    for i in range(M):  # 2명씩 묶어 지목된 사람을 같은 조로 병합
        union(arr[i*2], arr[i*2+1])

    # 각 사람의 대표자를 도출. set에 넣어 중복 제거
    sets = set(find_set(i) for i in range(1, N + 1))

    print(f'#{tc} {len(sets)}')  #set 길이 출력
