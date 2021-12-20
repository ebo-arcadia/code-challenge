# how to insert a new node at the beginning of a list?
# algorithms
# 1. define a class represents a node in the list. it has two properties, one value and the other pointing to the next node
# 2. define a class for creating linked list, with two nodes, head and tail, two methods push_node() and display()
# 3. push_node() will add node to the beginning of the linked list; display() will show all nodes in the list

# how to insert a new node between two nodes in a list?
# see add_node_to_mid for algorithms

# how to insert a new node at the end of a list?
# algorithms
# point the pointer of the current node to the inserted new node
# so that the current last node becomes the second last node and the new node becomes the new last node
# then point the pointer of the new last node to the head node in the list

# how to remove a node from a list?
# algorithms
# check if the list is empty
# if list is empty, returns the list is empty
# if list is not empty, check if the list only has one node, if so, set both head and tail nodes as null
# if the list has more than one node, calculate the midpoint, stores it in a variable
# maintain two variables, temp to store the node to be removed, previous to store node before the temp
# iterate the list till temp reaches the mid point (temp point at the mid point)
# remove temp so that previous next can point to temp next which point to the next node of temp

class Node:
    # represent node of list
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # declare head and tail pointer
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.size = 0

    def push_node(self, value):
        # create new node to be added
        newNode = Node(value)
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
        self.size += 1

    def append_node(self, value):
        newNode = Node(value)  # create a new node to be added
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # if list is not empty
            # make current tail pointing to the new node
            # make the new node the new tail node
            # point the new tail node to the head since the list is a circular linked list
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
        self.size += 1

    def add_node_in_mid(self, value):
        newNode = Node(value)
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # change the next pointer of the new node to the next pointer of the current middle node
            count = self.size // 2 if self.size % 2 == 0 else (self.size + 1) // 2
            # create temp pointing to the head node
            # create current pointing to the previous node of temp node
            temp = self.head
            current = temp
            for i in range(0, count):
                # iterate the list till middle point by incrementing temp to temp.next (recursion) till mid point (
                # end of the range)
                temp = temp.next
                # current will point to the new node
                current.next = newNode
            # insert newNode at the mid point so that current will point to it and such new node will point to temp
            newNode.next = temp
        self.size = self.size + 1

    def delete_node_mid(self):
        if self.head == None:
            return "the list is empty"
        else:
            # store middle point in a varaible called count
            count = self.size // 2 if self.size % 2 == 0 else (self.size + 1) // 2
            if self.head != self.tail:
                temp = self.head
                prev = None
                for i in range(0, count - 1):
                    prev = temp
                    temp = temp.next
                if prev != None:
                    # temp is the node to be deleted
                    # thus, previous node points to the the node next to temp by pointing to temp.next
                    prev.next = temp.next
                    # delete the mid point
                    del temp
                else:
                    self.head = self.tail = temp.next
                    self.tail.next = self.head
                    del temp
            # the list only contains one element
            else:
                self.head = self.tail = None
        self.size = self.size - 1

    def display(self):
        # define a current that will point to the head
        # print current.value till current node points to head again
        # current node points to the next node in the list in each iteration
        current_node = self.head
        current_list = []
        if self.head is None:
            print("linked list is empty")
            return "list is empty"
        else:
            # print each node value by incrementing the pointer
            print("Adding notes to the linked list: ")
            print(current_node.value)
            while current_node.next != self.head:
                current_node = current_node.next
                print(current_node.value)
                current_list.append(current_node.value)
            print("\n")
        return current_list


if __name__ == "__main__":
    list1 = LinkedList()

    list1.push_node(1)
    list1.display()  # display list after adding 1

    list1.push_node(10)
    list1.display()  # display list after adding 10

    list1.push_node(999)
    list1.display()  # display list after adding 999

    list1.push_node(87654)
    list1.display()  # display list after adding 87654
    list1.append_node(87654)
    list1.display()

    list1.add_node_in_mid(1000100001)
    list1.display()

    while list1.head != None:
        list1.delete_node_mid()
        print("Updated list: ")
        list1.display()
