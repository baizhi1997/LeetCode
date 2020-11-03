
# @Title: 旋转字符串 (Rotate String)
# @Author: qinxinlei
# @Date: 2018-10-23 15:58:52
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A)==len(B) and B in A+A
