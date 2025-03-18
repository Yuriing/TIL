import heapq

arr = [20, 15, 19, 4, 13, 11]

# 기본 리스트를 heap 으로 만들기
heapq.heapify(arr)  # 최소 힙으로 바뀐다
# 디버깅 시에 이진트리로 그림을 그려야 한다

# 하나씩 데이터를 추가한다
min_heap = []
for num in arr:
    heapq.heappush(min_heap, num)

print(min_heap)

# 최대 힙?
max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)

while max_heap:
    pop_num = heapq.heappop(max_heap)
    print(-pop_num, end=' ')
