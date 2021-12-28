# what is heap? a special tree data structure in which each parent node is less than or equal to its child nodes
# what is the benefit of using it? to represent priority queue which is also called heap queue
# what is the difference between priority queue (heap queue) and heap?
# a heap is a data structure whereas priority queue is an abstract datatype desribe a particular behaviors but not
# underline implementation

from binarytree import heap, build
import heapq

# how to create a heap in python?

random_max_heap_tree = heap()
print("\n random max heap tree: ", random_max_heap_tree)

max_heap_tree_height_3 = heap(2)
print("\n random max heap tree height 2: ", max_heap_tree_height_3)

min_perfect_heap_tree_height_3 = heap(3, is_max=False, is_perfect=True)
print("\n min perfect heap tree with height 3: ", min_perfect_heap_tree_height_3)

# how to create a heap (priority queue) using a list of elements?

print("-------------------------")
a_list = [31, 1, 9, 11, 5, 21]
heapq.heapify(a_list)
print("convert a list to a heap queue: ", a_list)
print(type(a_list))
heap_with_list = build(a_list)
print("\n heap tree created with a list: ", heap_with_list)
print("verify heap tree type: ", type(heap_with_list))

# what operations are support with heap queue (priority queue)
# insertion, replace, remove, push, pop
# 

heapq.heappush(a_list, 100)
print("pushed 100 to the heap queue: ", a_list)

heapq.heappop(a_list)
print("removed 1 from the heap queue: ", a_list)

heapq.heapreplace(a_list, 999)
print("remove the smallest / first element & insert 999 not fixed by any order: ", a_list)

heapq.heappushpop(a_list, 888)
print(a_list, end="")
print("----------------------")

print("return the largest 3 nums from a_list", end="")
print(heapq.nlargest(3, a_list))
print("return the smallest 2 nums from a_list", end="")
print(heapq.nsmallest(2, a_list))









