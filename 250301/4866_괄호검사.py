import sys
sys.stdin = open('input4866.txt')

dic = {'(':')', '[':']', '{':'}'}

def check(t_str):

    stack = []

    for i in t_str:
        if i in '([{':
            stack.append(i)
            continue
        elif i in ')]}':
            if len(stack) == 0:
                return 0
            elif len(stack) > 0 and i != dic[stack[-1]]:
                return 0
            elif len(stack) > 0 and i == dic[stack[-1]]:
                stack.pop()
                continue
    
    if len(stack) == 0:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    
    t_str = list(map(str, input().strip()))
    result = check(t_str)

    print(f'#{tc} {result}')