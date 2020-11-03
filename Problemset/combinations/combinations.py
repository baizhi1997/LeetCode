
# @Title: 组合 (Combinations)
# @Author: qinxinlei
# @Date: 2018-10-16 14:41:00
# @Runtime: 136 ms
# @Memory: N/A

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n<k:
            return []
        if n==k:
            return [list(range(1,n+1))]
        if k==1:
            return [[i] for i in range(1,n+1)]
        return self.combine(n-1,k)+[i+[n] for i in self.combine(n-1,k-1)]
