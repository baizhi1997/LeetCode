
# @Title: 不同的二叉搜索树 (Unique Binary Search Trees)
# @Author: qinxinlei
# @Date: 2018-10-15 15:25:55
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=1
        for i in range(2,n+1):
            ans=ans*(n+i)/i
        return round(ans)
