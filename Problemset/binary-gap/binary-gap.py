
# @Title: 二进制间距 (Binary Gap)
# @Author: qinxinlei
# @Date: 2018-11-08 18:54:17
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        x=100
        ans=0
        for i,c in enumerate(bin(N)):
            if c=='1':
                ans=max(ans,i-x)
                x=i
        return ans
