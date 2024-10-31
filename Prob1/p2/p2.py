import heapq
import sys

N = int(input())
nums = [int(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
max_heap = [-nums[0]]
min_heap = [nums[1]]
print(-max_heap[0])

if -max_heap[0] > min_heap[0]:
    tmp = max_heap[0]
    max_heap[0] = -min_heap[0]
    min_heap[0] = -tmp
print(-max_heap[0])
for i in range(2, N):
    num = nums[i]
    if i%2:
        heapq.heappush(min_heap, num)
    else:
        heapq.heappush(max_heap, -num)
    if -max_heap[0] > min_heap[0]:
        max_root = heapq.heappop(max_heap)
        min_root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_root)
        heapq.heappush(min_heap, -max_root)
    # print(max_heap, min_heap)
    print(-max_heap[0])
    