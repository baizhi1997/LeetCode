
# @Title: 宝石与石头 (Jewels and Stones)
# @Author: qinxinlei
# @Date: 2018-10-17 18:31:26
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans=0
        for s in S:
            if s in J:
                ans+=1
        return ans
