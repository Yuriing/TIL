# path = []
# lst = []
# used = [False] * 6
# count = 0
# result = False
# arr = list(map(int, input().split()))
#
#
# def recur(cnt):
#     global count
#     global result
#     if cnt == 6:
#         if path[0] == path[1] == path[2]:
#             count += 1
#         elif path[0] == path[1] - 1 == path[2] - 2:
#             count += 1
#
#         if path[3] == path[4] == path[5]:
#             count += 1
#         elif path[3] == path[4] - 1 == path[5] - 2:
#             count += 1
#
#         if count == 2:
#             result = True
#             return
#
#     for num in range(6):
#         if used[num]:
#             continue
#
#         used[num] = True
#         path.append(arr[num])
#         recur(cnt+1)
#         path.pop()
#         used[num] = False
#
#
# recur(0)
# if result:
#     print('Baby Gin!')
# else:
#     print('Try again!')

'''
다른 방식...
'''
lst1 = []
def babygin(selected, remain):
    if not remain:
        lst1.append(selected)
        return

    for i in range(len(remain)):
        pick = remain[i]
        new_remain = remain[:i] + remain[i+1:]
        babygin(selected + [pick], new_remain)
    return lst1


arr = list(map(int, input().split()))
lst2 = babygin([], arr)
count = 0
for lst3 in lst2:
    if lst3[0] == lst3[1] == lst3[2]:
        count += 1
    elif lst3[0] == lst3[1] - 1 == lst3[2] - 2:
        count += 1

    if lst3[3] == lst3[4] == lst3[5]:
        count += 1
    elif lst3[3] == lst3[4] - 1 == lst3[5] - 2:
        count += 1

    if count == 2:
        print('Baby Gin!')
        break
else:
    print('Try again!')

