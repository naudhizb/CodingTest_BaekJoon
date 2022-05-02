

import heapq

#파이썬에서 힙은 최소힙으로 구현되어 있습니다.
#pop 시 최솟값이 반환됩니다.

my_list = [4, 5, 6]

#list to heap
heapq.heapify(my_list)
heap = my_list[:] # Deepcopy

# push
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 30)

#pop
print(heap)
print(heapq.heappop(heap))
print(heap)
print("My List:", my_list)

