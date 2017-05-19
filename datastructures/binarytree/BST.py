
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

def find(node, value):
    if node is None:
        return False

    if node['value'] == value:
        return True
    elif node['value'] > value:
        return find(node['left'], value)
    else:
        return find(node['right'], value)

def smallest(node):
    if node['left'] is None:
        return node['value']
    else:
        smallest(node['left'])

def delete(node, value):
    if node is None:
        return None

    if node['value'] == value:
        # Case 1: leaf node
        if node['left'] is None and node['right'] is None:
            return None
        
        # Case 2: single child
        if node['left'] is None:
            return node['right']
        
        if node['right'] is None:
            return node['left']

        # Case 3: middle node with both childs
        smallest_on_right = smallest(node['right'])
        node['right'] = delete(node['right'], smallest_on_right)
        node['value'] = smallest_on_right
        return node

    elif node['value'] > value:
        node['left'] = delete(node['left'], value)
        return node
    else: # node['value'] < value
        node['right'] = delete(node['right'], value)
        return node
