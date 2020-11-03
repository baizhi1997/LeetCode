
# @Title: 较大分组的位置 (Positions of Large Groups)
# @Author: qinxinlei
# @Date: 2018-11-06 14:29:41
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans=[]
        i=0
        cur=' '
        for j,c in enumerate(S+' '):
            if c!=cur:
                cur=c
                if j-i-3>=0:
                    ans.append([i,j-1])
                i=j
        return ans
