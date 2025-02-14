# # 01 스택 구현
# top = -1
# stack = [0] * 10

# # push(1)
# top += 1
# stack[top] = 1

# # push(2)
# top += 1
# stack[top] = 2

# # push(3)
# top += 1
# stack[top] = 3

# # pop
# top -= 1
# print(stack[top+1])


# # 02 괄호의 짝 검사 프로그램
# txt = input()

# top = -1
# stack = [0] * 100

# ans = 1  # 짝이 맞다고 우선 가정
# for x in txt:
#     if x == '(':  # 여는 괄호 push
#         top += 1
#         stack[top] = x
#     elif x == ')':  # 닫는 괄호인 경우
#         if top == -1:  # 스택이 비어있으면
#             ans = 0
#             break  # for x # 어디 break 인지 적어두면 디버깅이 수월함
#         else:
#             top -= 1  # 소괄호만 있으므로 비교작업 생략

# if top > -1:  # 여는 괄호가 남아있으면
#     ans = 0

# print(ans)


# # 03 피보나치함수 + 재귀호출 횟수
# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
    
# cnt = 0
# print(fibo(10), cnt)


# # 04 재귀호출 연습
# def f(i, N):
#     if i == N:  # 중단조건
#         return
#     else:  # 재귀호출
#         f(i+1, N)


# def f2(i, N):
#     if i == N:
#         return
#     else:
#         print(A[i])
#         f(i+1, N)

# A = [1, 2, 3]
# f2(0, 3)

# import sys
# sys.stdin = open('input1208.txt')

# for test_case in range(1, 11):
# # 덤프 횟수 dump
#     dump = int(input())

# # 상자 리스트
#     arr_box = list(map(int, input().split()))

#     i = 1

#     while i <= dump:
#         arr_box[arr_box.index(max(arr_box))] -= 1
#         arr_box[arr_box.index(min(arr_box))] += 1
#         i += 1

#     gap = max(arr_box) - min(arr_box)

#     print(f'#{test_case} {gap}')

# t_num, leng = input().split()
# leng = int(leng)

# print(t_num)
# print(type(leng))

num_dict = {'ZRO': 0,
            'ONE': 1,
            'TWO': 2,
            'THR': 3,
            'FOR': 4,
            'FIV': 5,
            'SIX': 6,
            'SVN': 7,
            'EGT': 8,
            'NIN': 9,
            }

# # lst = ['str', 'int', 'type']
# # print(*lst)

# lst2 = [1, 3, 6, 4, 7, 5, 9, 2]
# # lst2.sort()
# # print(lst2)
# print(f'# {str(lst2)}')
print(num_dict['SIX'])