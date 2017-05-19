
# This is a hackaton binary tree

def node(value):
    """Create a node"""
    return {
        'left': None,
        'right': None,
        'value': value
    }

def visit_in_order(node, visitor):
    """Visit nodes in order (left, current, right)"""
    if node is None:
        return
    visit_in_order(node['left'], visitor)
    visitor(node['value'])
    visit_in_order(node['right'], visitor)

def height(node):
    """Calculate tree height"""
    if node is None:
        return 0
    return 1 + max(height(node['left']), height(node['right']))

def is_balanced(node):
    """Return a tuple (balanced, height) if balanced is True means that for each node the height of
    left and right do not differ more than 1"""
    if node is None:
        return (True, 0)

    lh = is_balanced(node['left'])
    lr = is_balanced(node['right'])

    balanced = lh[0] and lr[0] and (abs(lh[1] - lr[1]) <= 1)
    return (balanced, 1 + max(lh[1], lr[1]))

