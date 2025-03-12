# import sys
# sys.stdin = open('input2115.txt')


# 아우어베이커리 까눌레 정말 맛없어요...
# 일꾼 한 명이 특정 구간을 선택했을 때 해당 구간에서 나올 수 있는 최대 수익을 함수로 정의
def honey_max(lst_honey, M, C):
    # 일꾼 한 명이 선택한 구간에서 나올 수 있는 부분집합 전부 도출
    lst = []
    for i in range(1<<M):
        arr = []
        for j in range(M):
            if i & (1<<j):
                arr.append(lst_honey[j])
        lst.append(arr)

    # C 보다 작거나 같은 경우에만 제곱수를 도출해 최대값 반환
    max_val = 0
    for arr in lst:
        val = 0
        if sum(arr) > C:
            continue
        else:
            for c in arr:
                val += (c**2)
        max_val = max(max_val, val)

    return max_val


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())

    matrix_honey = []
    for _ in range(N):
        matrix_honey.append(list(map(int, input().split())))

    max_honey = 0
    for first_i in range(N):  # 첫 번째 일꾼이 구간 먼저 선택
        for first_j in range(N-M+1):
            first_honey = matrix_honey[first_i][first_j:first_j+M]

            # 첫 번째 일꾼이 선택한 구간에서 나올 수 있는 최대 수익
            first_max = honey_max(first_honey, M, C)

            for second_i in range(first_i, N):  # 두 번째 일꾼이 구간 선택
                for second_j in range(N-M+1):
                    if first_i == second_i and second_j < first_j+M:  # 첫 번째 일꾼이 선택한 구간 제외
                        continue
                    else:
                        second_honey = matrix_honey[second_i][second_j:second_j+M]
                        
                        # 두 번째 일꾼이 선택한 구간에서 나올 수 있는 최대 수익
                        second_max = honey_max(second_honey, M, C)

                        # 두 일꾼이 선택한 구간마다 비교하여 최대값 갱신
                        max_honey = max(max_honey, (first_max+second_max))

    print(f'#{tc} {max_honey}')
