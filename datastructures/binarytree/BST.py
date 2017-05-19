
"""
Binary Search Tree
"""

import BinaryTree

def add(node, value):
    """Add a node on the root of BST"""
    if node is None:
        return BinaryTree.node(value)

    if node['value'] > value:
        node['left'] = add(node['left'], value)
        return node
    elif node['value'] < value:
        node['right'] = add(node['right'], value)
        return node
    else:
        return node

def is_bst(node):
    """Return true if BST"""
    if node is None:
        return True
    
    if node['left'] is None or node['right'] is None:
        return True

    if node['left']['value'] < node['value'] and node['right']['value'] > node['value']:
        return True
    
    return False
