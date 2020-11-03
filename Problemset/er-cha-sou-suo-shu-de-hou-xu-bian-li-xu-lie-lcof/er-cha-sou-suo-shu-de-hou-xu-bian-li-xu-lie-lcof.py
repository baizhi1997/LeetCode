
# @Title: 二叉搜索树的后序遍历序列 (二叉搜索树的后序遍历序列 LCOF)
# @Author: qinxinlei
# @Date: 2020-07-04 01:47:38
# @Runtime: 32 ms
# @Memory: 13.4 MB

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True

