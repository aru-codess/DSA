# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        first_null_hit = False

        while q:
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)

                if first_null_hit:
                    return False

            else:
                first_null_hit = True

        return True
