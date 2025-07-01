# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node: Optional[TreeNode], arr: list):
        if node is None:
            arr.append(None)
            return
        arr.append(node.val)
        self.traverse(node.left, arr)
        self.traverse(node.right, arr)
        return arr

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = self.traverse(p, [])
        arr2 = self.traverse(q, [])
        return arr1 == arr2