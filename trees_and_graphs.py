class Node:
    def _init__(self, val, left=None, right=None):
        self.val = val
        self.children = [left,right]
def in_order_traversal(node):
    if not node:
        in_order_traversal(node.left)
        print(node.val)
        in_order_traversal(node.right)
def pre_order_traversal(node):
    if not node:
        print(node.val)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
def post_order_traversal(node):
    if not node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val)
