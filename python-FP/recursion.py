# many loops construction can be replaced by recursion

# example
# check if a certain value is in a tree data structure

class Tree:
    def __int__(self):
        self.value = None
        self.left = None
        self.right = None

    # imperative approach using while loop and a stack
    def contains_nodes(self, tree, value):
        data_tree = [tree] # a list of nodes to visit
        while data_tree:
            node = data_tree.pop()
            if node is None:
                continue
            elif node.val == value:
                return True
            else:
                data_tree.append(node.left)
                data_tree.append(node.right)
        return False

    # declarative approach with resurision
    # function find_nodes keeps calling itself as long as there are nodes in the tree

    def find_node(self, tree, node):
        # base case
        if tree is None:
            return False

        return (tree.value == node
                or find_node(self, tree.left, node)
                or find_node(self, tree.right, node))
