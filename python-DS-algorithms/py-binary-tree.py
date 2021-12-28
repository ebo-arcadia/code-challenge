# what is a binary tree? a data structure with every node or vertex has almost two children
# what is the representation of a binary tree in python?

from binarytree import Node, build, tree, bst

# how to create a binary tree in python?

root_node = Node(3)
root_node.left = Node(6)
root_node.right = Node(10)

print("\n getting binary tree: ", root_node)
print("\n getting list of nodes: ", list(root_node))
print("\n getting inorder of nodes: ", root_node.inorder)
print("\n size of the tree properties: ", root_node.size)
print("\n height of the tree properties: ", root_node.height)
print("\n check all the tree properties: ", root_node.properties)
print("----------------------------")

# how to convert a list to a binary tree?

nodes_list = [11, 3, 5, 7, 8, 9, None, 13, 29]
binary_tree = build(nodes_list)
print("\n getting binary tree: ", binary_tree)
print("\n getting list of nodes: ", binary_tree.value)

# how to build a random binary tree?

random_tree_any_height = tree()
print("\n random tree with any height: ", random_tree_any_height)

random_tree_height_three = tree(4)
print("\n random tree with height 3: ", random_tree_height_three)

random_perfect_tree_height_three = tree(3, is_perfect=True)
print("\n random perfect tree with height 3: ", random_perfect_tree_height_three)

# what is a binary search tree? a special tree structure which inorder gives a sorted list of nodes or vertices
# how to create a binary search tree?

bin_sear_tree_height_three = bst(3, is_perfect=False)
print("\n binary search tree with height 3: ", bin_sear_tree_height_three)

perfect_bin_sear_tree_height_two = bst(2, is_perfect=True)
print("\n binary search tree with height 3: ", perfect_bin_sear_tree_height_two)
