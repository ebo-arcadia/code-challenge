# what is a queue data structure?
# it is a collection of objects that support first in
# first out semantics (FIFO) for inserts and delete operations
# it is a linear data structure stores data items in first in first out manner
# what ways can queue be implemented? list, collections.deque. queue.Queue

# example
# create a queue class to implement the first in first out semantics

class Queue:
    def __init__(self):
        self.queue = list()

    def insert_to_start(self, item):
        if item not in self.queue:
            self.queue.insert(0, item)
            return True
        else:
            return False

    def remove_from_queue(self):
        if len(self.queue) > 0:
            removed = self.queue.pop()
            print("{} is removed".format(removed))
            return self.queue
        else:
            return "no element to be removed"

    # below operation not good practice because it is not first in first out

    # def insert_to_end(self, item):
    #     if item not in self.queue:
    #         self.queue.insert(len(self.queue), item)
    #         return True
    #     else:
    #         return False

    def query_queue(self):
        return self.queue


if __name__ == "__main__":
    queue1 = Queue()
    queue1.insert_to_start("item1")
    queue1.insert_to_start("item2")
    queue1.insert_to_start("item3")
    queue1.insert_to_start("item4")
    queue1.insert_to_start("item5")
    queue1.insert_to_start("item6")
    query_q = queue1.query_queue()
    print("current queue: ", query_q)
    queue1.remove_from_queue()
    query_q = queue1.query_queue()
    print("current queue: ", query_q)
