# Definition for
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p != None and q == None) or (p == None and q != None):
            return False
        elif (p == None and q == None):
            return True
        elif p.val != q.val:
            return False
        else:
            left_flag = self.isSameTree(p.left, q.left)
            right_flag = self.isSameTree(p.right, q.right)
            return left_flag and right_flag


p = TreeNode(1, None, None)
p.left = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(None)
q.right = TreeNode(2)

ans = Solution()
print(ans.isSameTree(p, q))
# def check(p, q):
#     if p.val != q.val:
#         return False
#     else:
#         left_flag = check(p.left, q.left)
#         right_flag = check(p.right, q.right)
#         return left_flag == right_flag
