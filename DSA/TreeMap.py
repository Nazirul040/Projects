
class TreeMap:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


def insert(key, data, tree):
    if tree is None:
        return TreeMap(key, data)
    
    if key < tree.key:
        tree.left = insert(key, data, tree.left)
    elif key > tree.key:
        tree.right = insert(key, data, tree.right)
    else:
        tree.data = data

    return tree


def find(tree, key):
    if tree is None:
        return None
    
    if key < tree.key:
        return find(tree.left, key)
    elif key > tree.key:
        return find(tree.right, key)
    else:
        return tree.data


def height(tree):
    if tree is None:
        return 0
    
    return 1 + max(height(tree.left), height(tree.right))


def size(tree):
    if tree is None:
        return 0
    
    return 1 + height(tree.left) + height(tree.right)


def inorder_traversal(tree):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        return tree.key
    
    return [inorder_traversal(tree.left)] + [tree.key] + [inorder_traversal(tree.right)]


def preorder_traversal(tree):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        return tree.key
    
    return [tree.key] + [preorder_traversal(tree.left)] + [preorder_traversal(tree.right)]


def postorder_traversal(tree):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        return tree.key
    
    return [preorder_traversal(tree.left)] + [preorder_traversal(tree.right)] + [tree.key]


def min_max(tree):
    if tree is None:
        return 'zzzzz', 'aaaaa'

    left_min, left_max = min_max(tree.left)
    right_min, right_max = min_max(tree.right)

    curr_min = min(tree.key, left_min, right_min)
    curr_max = max(tree.key, left_max, right_max)

    return curr_min, curr_max


def delete(tree, key):
    if key < tree.key:
        if tree.left:
            tree.left = delete(tree.left, key)
    elif key > tree.key:
        if tree.right:
            tree.right = delete(tree.right, key)
    else:
        if tree.left is None:
            return tree.right
        elif tree.right is None:
            return tree.left
        else:
            min_larger_node = min_max(tree)[0]
            tree.key, tree.data = min_larger_node.key, min_larger_node.data
            tree.right = delete(tree.right, min_larger_node.key)

    return tree


def display(root):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if root.right is None and root.left is None:
        line = '%s' % root.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = display(root.left)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = display(root.right)
        s = '%s' % root.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display(root.left)
    right, m, q, y = display(root.right)
    s = '%s' % root.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def print_tree(root):
    lines, *_ = display(root)
    for line in lines:
        print(line)


if __name__ == '__main__':
    tree = None
    
    data = {
        'nazirul': ['Sk Nazirul Islam', 'JGEC', '1st Year'],
        'sagnik': ['Sagnik Roy Chowdhury', 'KIIT University', '1st Year'],
        'sohom': ['Sohom Mondol', 'KIIT University', '1st Year'],
        'manandip': ['Manandip Das', 'KGEC', '1st year'],
        'satwik': ['Satwik Chandra', 'KIIT', '1st Year']
    }

    tree = insert('nazirul', data['nazirul'], tree)
    tree = insert('sagnik', data['sagnik'], tree)
    tree = insert('sohom', data['sohom'], tree)
    tree = insert('manandip', data['manandip'], tree)
    tree = insert('satwik', data['satwik'], tree)

    print_tree(tree)
    print(find(tree, 'sohom'))
    print(height(tree))
    print(size(tree))
    print(inorder_traversal(tree))
    print(preorder_traversal(tree))
    print(postorder_traversal(tree))
    print(f"Minimum : {min_max(tree)[0]} and Maximum : {min_max(tree)[1]}",)
    print_tree(delete(tree, 'sagnik'))