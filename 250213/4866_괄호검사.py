import sys
sys.stdin = open('input3.txt')

T = int(input())

open_lst = ['(', '{', '[']
close_lst = [')', '}', ']']


def bracket_test(t_str):
    stack = []  # 빈 스택 필요
    for char in t_str:
        if char in open_lst:  # 여는 괄호면
            stack.append(char)

        elif char in close_lst:  # 닫는 괄호면
            # 빈 스택인지 검사
            if len(stack) == 0:
                return 0  # 정상적으로 짝을 이루지 않았다 # for char 종료
            # 빈 스택이 아니면
            elif len(stack) != 0:  # 스택에 들어온 괄호가 있을 경우
                top_char = stack.pop()
                '''
                괄호만 stack 에 넣어 검사하기 때문에
                괄호 이외의 다른 문자는 신경쓰지 않음.
                '''
                for n in range(3):  # 괄호의 쌍이 다른 것일 경우
                    if char == open_lst[n] and top_char != close_lst[n]:
                        return 0  # for char 종료

        else:  # 괄호가 아닐 경우
            continue
    # pop 을 다 했다면
    if len(stack) == 0:  # stack 에 남은 것이 없을 경우
        return 1
    else:
        return 0


for tc in range(1, T + 1):
    print(f'#{tc} {bracket_test(input())}')