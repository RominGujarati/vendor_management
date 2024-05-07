class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallestElement(root: TreeNode, k:int):
    stack = []
    count = 0

    while root in stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        count += 1
        if count == k:
            return root.val
        root = root.right

    return -1

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

k = 1
res = kthSmallestElement(root, k)