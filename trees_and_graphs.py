class Node:
    def _init__(self, val, children=None):
        self.val = val
        self.children = children
def in_order_traversal(node):
    if not node:
        in_order_traversal(node.children[0])
        print(node.val)
        in_order_traversal(node.children[1])
def pre_order_traversal(node):
    if not node:
        print(node.val)
        pre_order_traversal(node.children[0])
        pre_order_traversal(node.children[1])
def post_order_traversal(node):
    if not node:
        post_order_traversal(node.children[0])
        post_order_traversal(node.children[1])
        print(node.val)
