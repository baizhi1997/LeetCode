
# @Title: 优美的排列 II (Beautiful Arrangement II)
# @Author: qinxinlei
# @Date: 2018-12-09 14:28:06
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        l=1
        for _ in range(k//2):
            ans.append(l)
            l+=1
            ans.append(n)
            n-=1
        if k&1:
            return ans+list(range(l,n+1))
        return ans+list(range(n,l-1,-1))
