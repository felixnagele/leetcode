from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        root_node: int = root.val
        left_child: int = root.left.val
        right_child: int = root.right.val
        sum_of_childs = left_child + right_child
        return sum_of_childs == root_node
