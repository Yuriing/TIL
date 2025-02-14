# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
# def dfs(v, N):
#     visited = [0] * (N+1)
#     stack = []

#     while True:
#         if visited[v] == 0:  # 첫 방문이면
#             visited[v] = 1
#             print(v)
#         for w in adj_list[v]:  # v에 인접하고 방문 안 한 w가 있으면
#             if visited[w] == 0:
#                 stack.append(v)
#                 v = w
#                 break  # for w
#         else:
#             if stack:
#                 v = stack.pop()
#             else:
#                 break


# V, E = map(int, input().split())
# graph = list(map(int, input().split()))
# adj_list = [[] for _ in range(V+1)]

# for i in range(E):
#     v, w = graph[i*2], graph[i*2+1]

#     adj_list[v].append(w)
#     adj_list[w].append(v)

lst = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
N = 5
n = N//2

print(lst[0][-1:-3:-1])

# for list in lst:
#     print(list[0:n])
#     n = n - 1
#     if n == 0:
#         break

# num1 = N//2
# harvest = 0
# for n in range(N//2):
#     harvest = int(sum(lst[n]) - (sum(lst[n][0:num1]) + sum(lst[n][-1:-num1-1:-1])))
#     num1 -= 1
#     if num1 == 0:
#         break

# harvest += int(sum(lst[N//2]))

# num2 = 0
# for n in range(N//2+1, N):
#     harvest += int(sum(lst[n]) - (sum(lst[n][0:num2]) + sum(lst[n][-1:-num2-1:-1])))
#     num2 += 1
#     if num2 == N//2:
#         break



# print(harvest)