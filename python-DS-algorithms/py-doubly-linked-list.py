# what is doubly linked list and why use it?
# it is a linked list with every node that has an additional pointer pointing to
# its previous node in addition to the pointers for the next node
# it makes easier for reserve traverse

# advantages and disadvantages of doubly linked list versus singly linked list?
# faster with insertion and deletion but requires extra space

# operations
# push, append, search, insert after, insert before, delete

# creating doubly linked list

# 1. create a node class
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


# 2. create a doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # function to add a node at the front of the list
    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            return "previous node does not exist"

        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        # change the previous of the new_node's next node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(data=new_data)

        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def printList(self, node):

        print("\n Traverse in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node.next

        print("\n Traverse in reverse direction")
        while last:
            print(" {}".format(last.data))
            last = last.prev


if __name__ == "__main__":
    ddl = DoublyLinkedList()
    ddl.push("item1")
    ddl.push("item2")
    ddl.append("item10")
    ddl.append("item99")
    ddl.insertAfter(ddl.head.next, "item1000")
    print("created ddl is: ")
    ddl.printList(ddl.head)

