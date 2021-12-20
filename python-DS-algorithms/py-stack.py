# what is a stack?
# it means to arrange objects on top of each other

# how data is arranged in a stack? in a stack, element inserted last will come out first (LIFO - last in first out)
# what is the top of a stack? In a stack, one can only add and remove element from this top / end of a stack
# stack operations: push and pop

# example
# implement stack operations using array

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            # use built-in append() to add an element to the stack
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove_top(self):
        if len(self.stack) <= 0:
            return "the stack is empty. nothing to remove"
        else:
            # using built-in pop() to remove the top element of the stack
            self.stack.pop()

    def clear_stack(self):
        while len(self.stack) > 0:
            self.stack.pop()

    def peek_stack(self):
        return self.stack

    def peek_stack_top(self):
        return self.stack[-1]


if __name__ == "__main__":
    a_stack = Stack()
    a_stack.add("element 1")
    a_stack.add("element 2")
    a_stack.add("element 3")
    stack_top_info = a_stack.peek_stack_top()
    stack_info = a_stack.peek_stack()
    print("top element in the stack: ", stack_top_info)
    print("full stack: ", stack_info)
    print("------------------------")
    updated = a_stack.remove_top()
    print("full stack after removing the top element: ", stack_info)
    print("------------------------")
    a_stack.add("element 4")
    a_stack.add("element 5")
    a_stack.add("element 6")
    print("full stack: ", stack_info)
    a_stack.clear_stack()
    print("full stack after removing all elements: ", stack_info)
