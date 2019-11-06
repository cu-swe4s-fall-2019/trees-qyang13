class Node:
    def __init__(self, key, value=None, left=None, right=None):
        '''
        Initialization function to create a node object for the binary tree
        ---
        key - the key for the node, integer
        value - the value associated with the key, could potentially be any type
        left - the left branch, key value should be smaller
        right - the right branch, key value should be larger
        '''
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value=None):
    '''
    Function to add key and value to a binary tree
    ---
    key - the key for the node, integer
    value - the value associated with the key
    '''
    if root == None:
        root = Node(key, value=value)
        return root
    else:
        if key < root.key:
            if root.left == None:
                root.left = Node(key, value=value)
            else:
                insert(root.left, key, value=value)
        else:
            if root.right == None:
                root.right = Node(key, value=value)
            else:
                insert(root.right, key, value=value)
        return root


def search(root, key):
    '''
    Function to search a key in the binary tree, returns the associated value
    ---
    key - the key for the node, integer
    '''
    # Either the tree is empty or the specific key is not found
    if root == None:
        return None
    else:
        if key == root.key:
            return root.value
        elif key < root.key:
            return search(root.left, key)
        elif key > root.key:
            return search(root.right, key)
