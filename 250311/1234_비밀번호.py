import sys
sys.stdin = open('input1234.txt')

for t in range(1, 11):
    N, M = map(str, input().split())
    N = int(N)

    stack = []
    for i in range(N):
        if len(stack) == 0:  # 빈 스택인지 검사
            stack.append(int(M[i]))
        else:  # 아니라면
            num = stack.pop()
            if num != int(M[i]):  # 불일치
                stack.append(num)  # 다시 넣기
                stack.append(int(M[i]))
            else:  # 일치
                continue  # 둘 다 보내고 계속 검사

    print(f'#{t} {"".join(map(str, stack))}')
