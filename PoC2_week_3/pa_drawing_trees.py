'''
EXPERIMENTS POC TREE: http://www.codeskulptor.org/#user43_GdK7HVS6b4_8.py
EXPERIMENTS POC DRAW TREE: http://www.codeskulptor.org/#user43_Rcfi2PA6t5_10.py
SOURCE POC TREE: http://www.codeskulptor.org/#poc_tree.py
SOURCE POC DRAW TREE: http://www.codeskulptor.org/#poc_draw_tree.py
'''


from poc_tree import Tree

NODE_HEIGHT = 4
NODE_WIDTH = 3

my_tree = Tree('a', [Tree('b', []), Tree('c', []), Tree('d', [Tree('e', [])])])
print my_tree

def get_box_size(tree):
    width, height = 0, 0
    children = tree.children()
    for child in children:
        current_width, current_height = get_box_size(child)
        width += current_width
        height = max(height, current_height)
    target_width = max(NODE_WIDTH, width)
    height += NODE_HEIGHT
    return target_width, height


def get_box_size1(tree):
    """
    Recursive function to compute height and width
    of the bounding box for a tree
    """
    current_subtree_widths = 0
    tree_height = 0
    for child in tree.children():
        child_width, child_height = get_box_size(child)
        current_subtree_widths += child_width
        tree_height = max(tree_height, child_height)
    subtree_width = max(NODE_WIDTH, current_subtree_widths)
    tree_height = NODE_HEIGHT + tree_height
    return subtree_width, tree_height


if __name__ == '__main__':
    print get_box_size(my_tree)
    print get_box_size1(my_tree)