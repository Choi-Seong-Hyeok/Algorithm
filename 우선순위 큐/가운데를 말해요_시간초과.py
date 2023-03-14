import sys
import heapq
import math
input = sys.stdin.readline

n = int(input())
heap = []
sub_heap = []
for i in range(n):
    val = int(input())
    if i == 0:
        heapq.heappush(heap, val)
        print(val)
    else:
        heapq.heappush(heap, val)
        heap.sort()
        if len(heap) % 2 == 0:
            f = len(heap) // 2
            fidx = f - 1
            print(heap[fidx])
        else:
            print(heap[len(heap)//2])
