import sys
sys.stdin = open('input4873.txt')

T = int(input())
for tc in range(1, T+1):
    
    lst = list(map(str, input().strip()))
    stack = []

    for char in lst:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{tc} {len(stack)}')