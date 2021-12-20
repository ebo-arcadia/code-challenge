# what is linked list?
# it is a sequence of data elements linked via links
# each data element has a pointer pointing toward another element
# no standard library in python but using the concept of node instead
# Node are the foundation for other data structures such as linked lists and tree

# singly linked lists: there is only one link between any two data elements

# how to create a linked list?

class Node:
    def __init__(self, nodeval=None):
        self.nodeval = nodeval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def listnodes(self):
        thisnode = self.headval
        stored_nodes = []
        while thisnode is not None:
            print("next node: ", thisnode.nodeval)
            stored_nodes.append(thisnode.nodeval)
            thisnode = thisnode.nextval
        return stored_nodes


list1 = LinkedList()

# create first node with a value 'religion' in the linked list
list1.headval = Node("religion")

node2 = Node("psychology")
node3 = Node("biology")
node4 = Node("economics")
node5 = Node("computer science")

# link the first node in the linked list (list1) to the second node
list1.headval.nextval = node2

# link the second node to the third node so on and so forth
node2.nextval = node3
node3.nextval = node4
node4.nextval = node5

# how to traverse a linked list?
# singly linked list can be only traversed in the forward direction staring from the first node
# print the value of the next element by assigning the pointer of the next element to the current data element
