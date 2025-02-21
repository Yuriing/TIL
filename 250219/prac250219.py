# # 01 Queue
# # 큐 생성
# queue = [0]*3
# front = rear = -1

# # 1, 2, 3 인큐
# rear += 1  # enQueue 1
# queue[rear] = 1

# rear += 1  # enQueue 2
# queue[rear] = 2

# rear += 1  # enQueue 3
# queue[rear] = 3

# while front != rear:  # 큐에 원소가 남아있으면
#     front += 1
#     t= queue[front]
#     print(t)
#     # 이런 식으로 검사하고 꺼내는 경우가 많음


# # # deQueue
# # front += 1
# # print(queue[front])  # 1

# # front += 1
# # print(queue[front])  # 2

# # front += 1
# # print(queue[front])  # 3
# # # 먼저 넣은 item이 먼저 나온다

# q = []
# q.append(1)  # enqueue 1
# q.append(2)  # enqueue 2
# q.append(3)  # enqueue 3
# print(q.pop(0))  # dequeue 1
# print(q.pop(0))  # dequeue 2
# print(q.pop(0))  # dequeue 3
# # 웬만해서 권장하는 방법은 아님...

lst = [1, 0, 0, 1, 1, 0]
if set(lst) < {0, 1}:
    print(True)
else:
    print(False)