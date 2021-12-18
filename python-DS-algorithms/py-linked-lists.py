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
print("--------------------")


# how to insert a new node at the beginning of a list?

# algorithms
# 1. define a class represents a node in the list. it has two properties, one value and the other pointing to the next node
# 2. define a class for creating linked list, with two nodes, head and tail, two methods addNodesAtBeginning() and display()
# 3. addNodesAtBeginning() will add node to the beginning of the linked list; display() will show all nodes in the list

class Nodes:
    # represent node of list
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedLists:
    # declare head and tail pointer
    def __init__(self):
        self.head = Nodes(None)
        self.tail = Nodes(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def addNodesAtBeginning(self, value):
        # create new node to be added
        newNode = Nodes(value)
        # check if the list is empty
        # if empty, point both the head and tail to the new node
        # the new node is also pointed to the head
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # if the list is not empty
            # store current first node in a temp var
            # new node points to the temp as the temp becomes the second / next node
            # new node becomes the new head
            # tail also points to the new node
            temp = self.head
            newNode.next = temp
            self.head = newNode
            self.tail.next = self.head

    def display(self):
        # define a current that will point to the head
        # print current.value till current points to head again
        # current points to the next node in the list in each iteration
        current_node = self.head
        current_list = []
        if self.head is None:
            print("linked list is empty")
            return "list is empty"
        else:
            # print each node value by incrementing the pointer
            print("Adding notes to the start of the list: ")
            print(current_node.value)
            while current_node.next != self.head:
                current_node = current_node.next
                print(current_node.value)
                current_list.append(current_node.value)
            print("\n")
        return current_list

# how to insert a new node at the end of a list?
# how to insert a new node between two nodes in a list?
# how to remove a node from a list?

if __name__ == "__main__":
    print("traverse the singly linked list1: ", list1.listnodes())
    print("--------------------------------")
    list1 = LinkedLists()
    list1.addNodesAtBeginning(1)
    list1.display()  # display list after adding 1
    list1.addNodesAtBeginning(10)
    list1.display()  # display list after adding 10
    list1.addNodesAtBeginning(999)
    list1.display()  # display list after adding 999
    list1.addNodesAtBeginning(8971)
    print("most current linked list: ", list1.display())
