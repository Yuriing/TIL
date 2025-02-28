import sys
sys.stdin = open('input1244.txt')

K = int(input())

# 받는 숫자 값을 인덱스값으로 활용하기 위해 맨 앞에 안 쓰는 요소 하나를 추가한다.
switch = [0]
lst = list(map(int, input().split()))

switch.extend(lst)

T = int(input())

# 학생 수 만큼 스위치 조작 반복
for p in range(T):
    S, n = map(int, input().split())

    if S == 1:  # 남자인 경우
        for i in range(1, K+1):
            if i % n == 0:  # 인덱스 넘버를 n으로 나눈 나머지가 0일 경우 스위치 조작
                if switch[i] == 0:
                    switch[i] = 1
                elif switch[i] == 1:
                    switch[i] = 0

    elif S == 2:  # 여자인 경우
        if switch[n] == 0:
            switch[n] = 1
        else:
            switch[n] = 0

        for i in range(1, K+1-n):
            if n-i <= 0 or n+i > K+1:
                break
            else:
                if switch[n-i] == switch[n+i]:
                    if switch[n-i] == 0 and switch[n+i] == 0:
                        switch[n-i] = switch[n+i] = 1
                    elif switch[n-i] == 1 and switch[n+i] == 1:
                        switch[n-i] = switch[n+i] = 0
                        continue
                else:
                    break

switch.pop(0)  # 맨 앞에 넣었던 요소 제거

if len(switch) < 20:
    print(*switch)
else:
    for i in range(len(switch)//20+1):
        if 20*(i+1) > len(switch):
            print(*switch[20*i:])
        else:
            print(*switch[20*i:20*(i+1)])
