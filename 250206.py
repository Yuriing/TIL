# 01 counting sort
def counting_sort(input_arr, max_val):
    '''
    input_arr: 입력 배열(정렬 전)
    입력 배열에서 각 원소는 0 이상 max_val 이하
    max_val: 입력 배열 내 원소 중 최대 값(데이터의 범위)
    '''
    # 빈도 수 기록용 배열 생성
    counting_arr = [0] * (max_val + 1)
    '''
    인덱스는 0부터 시작하므로 max_val과 같은 숫자까지 나오려면 +1 필요
    [0, 0, 0, 0, 0] 생성
    '''
    # 입력 배열 내 각 원소의 빈도 수를 counting_arr에 기록
    for num in input_arr:
        counting_arr[num] += 1
    '''
    counting_arr의 인덱스와 같은 num이 있을 경우
    counting_arr의 수를 1 올림
    [0, 2, 0, 1, 1]
    '''
    # 누적합 기록
    for i in range(1, max_val+1):
        counting_arr[i] += counting_arr[i-1]
    '''
    오른쪽 기준 왼쪽과 더하는 것이기 때문에 1부터 시작.
    맨 오른쪽까지 순회해야 하므로 max_val+1까지
    [0, 2, 2, 3, 4]
    여기에서 나온 원소가 최종 리스트에서 해당 인덱스 번호의 숫자가 가야 할 자리가 됨
    '''
    # 최종 위치를 기록할 결과 배열 생성
    result_arr = [0] * len(input_arr)
    '''
    [0, 0, 0, 0]
    '''
    # 최종 위치 결정
    # 입력 배열을 역순으로 반복하며 누적합 기준으로 원소 배치
    for number in reversed(input_arr):
        # 누적합에서 1 소진
        counting_arr[number] -= 1
        # 소진시킨 값을 인덱스로 활용하며 결과 배열에 최종 배치
        result_arr[counting_arr[number]] = number
    '''
    최종 리스트의 인덱스 번호는 '4번째 자리 > 3'과 같은 형태로 나오므로
    누적합 원소에서 -1을 한 번호를 인덱스 번호로 삼아 배치해야함
    [1, 1, 3, 4]
    '''
    return result_arr


# 02 구간합
T = int(input())  # 번호 생성

def prefix_sum(N, M, arr):
    '''
    (N - M)번째의 정수까지 range를 돌려야 하므로
    실제 range 범위는 그보다 1 많은 N-M+1까지
    '''
    new_arr = []
    for i in range(N - M + 1):
        '''
        arr[N]부터 arr[N+M-1]까지
        > M=5일 경우 인덱스 0, 1, 2, 3, 4
        >> 해당 구간을 슬라이스로 잡으면 4+1인 [:5]가 되므로
        슬라이스는 [i:i+M]
        '''
        plus = sum(arr[i:i+M])
        # 해당 합산 값을 새로운 리스트에 추가
        new_arr.append(plus)

    # 추가한 리스트에서 최대값과 최소값을 뽑아 감산한다
    return max(new_arr) - min(new_arr)
        
for tc in range(1, T+1):
    N = int(input())  # arr에서 주어지는 정수의 개수
    M = int(input())  # 구간의 개수
    arr = list(map(int, input().split()))  # 정수의 배열


    print(f'# {tc} {prefix_sum(N, M, arr)}')


# 03 숫자카드
T = int(input())  # 번호 생성

arr_list = [0] * 10
'''
카드에 적힌 숫자의 범위는 0<=a<=9
인덱스 번호가 0부터 9까지 모두 생성되도록 구간 10개 생성
'''
def max_card(arr):
    for num in arr:  # 숫자 a가 있을 시 인덱스 번호 a에 해당하는 구간 +1
        arr_list[num] += 1

    return arr_list.index(max(arr_list)), max(arr_list)

for tc in range(1, T+1):
    arr = list(map(int, input().split()))  # 카드 배열

    print(f'# {tc} {max_card(arr)}')


# 04 Baby Gin # 근데 왜 이름이 베이비진일까요...
card_list = []
arr = list(map(int, input().split()))  # 카드 배열

# 완전검색으로 풀이
for i1 in range(6):
    for i2 in range(6):
        if i1 != i2:
            for i3 in range(6):
                if i1 != i3 and i2 != i3:
                    for i4 in range(6):
                        if i1 != i4 and i2 != i4 and i3 != i4:
                            for i5 in range(6):
                                if i1 != i5 and i2 != i5 and i3 != i5 and i4 != i5:
                                    for i6 in range(6):
                                        if i1 != i6 and i2 != i6 and i3 != i6 and i4 != i6 and i5 != i6:
                                            card_list.append([arr[i1], arr[i2], arr[i3], arr[i4], arr[i5], arr[i6]])


# run과 triplet이 있다면 'Baby gin' 도출  # 강사님이 다른 방법을 알려주신 데엔 이유가 있군요...
result = False  # 기본값을 False로 두기

for lists in card_list:
    if ((lists[0] == lists[1] == lists[2] and (lists[3] + 2 == lists[4] + 1 and lists[4] + 1 == lists[5])) or 
        (lists[0] == lists[1] == lists[2] and lists[3] == lists[4] == lists[5]) or 
        ((lists[0] + 2 == lists[1] + 1 and lists[1] + 1 == lists[2]) and (lists[3] + 2 == lists[4] + 1 and lists[4] + 1 == lists[5]))):

        print('Baby gin')
        result = True  # 해당하는 경우 True로 바뀜
        break

if not result:  # True가 아닐 경우
    print('try again')


# 05 전기버스
count = []
K = 3
N = 10
arr = [1, 3, 5, 7, 9]

for i in range(1, N//K + 1):  # num이 다 움직일 동안 i가 안 움직인다는 문제가 있음
    for num in arr:
        if K * i < num:
            print(0)
            break
        else:
            count.append(1)

print(len(count))