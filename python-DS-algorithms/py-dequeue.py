# what is dequeue?
# what is the benefit of using it?
# how does dequeue get implemented?

# it is a double-ended queue data structure supporting adding and removing from both end
# it is implemented through the collections library
# deque is preferred than list because it provides quicker append or pop as the time complexity is O(1)

# create a deque
from collections import deque

a_deque = deque(['picture', 'video', 'paint'])
print("a deque: ", a_deque, ". Type is: ", type(a_deque))

num_deque = deque([10, 20, 30, 1, 500, 1, 2, 1, 333, 5, 199, 2, 21])

# operations

a_deque.append("insert this from the right")
a_deque.appendleft("insert this from the left")
print("updated deque: ", a_deque)
popped_elem_right = a_deque.pop()
print(popped_elem_right)
popped_elem_left = a_deque.popleft()
print(popped_elem_left)

print('how many times num 1 occurs in num_deque? ', num_deque.index(1, 2, len(num_deque)))
num_deque.insert(len(num_deque), -1)
print('updated num_deque after inserting -1 at the end: ', num_deque)
num_deque.remove(1)
print("updated num_deque after removing the first occurrence of 1: ", num_deque)
print("number of 2 in dequeue: ", num_deque.count(2))

# more operations
# extend(iterable)
a_deque.extend(["art", "music", "dance"])
print("updated a_deque extended iterable to the right: ", a_deque)
# extendleft(iterable)
a_deque.extendleft(["movie", "TV shows", "comedy"])
print("updated a_deque extended iterable to the left: ", a_deque)
# reverse()
a_deque.reverse()
print("reversed deque:", a_deque)
# rotate()
a_deque.rotate(2)
print("rotate a_deque by 2: ", a_deque)



