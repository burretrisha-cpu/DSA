# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        A = []
        def B(root,level):
            if not root:
                return
            if len(A)==level:
                A.append([])
            A[level].append(root.val)
            B(root.left,level+1)
            B(root.right,level+1)
        B(root,0)
        return A           