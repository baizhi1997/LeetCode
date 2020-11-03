
# @Title: 删列造序 (Delete Columns to Make Sorted)
# @Author: qinxinlei
# @Date: 2018-11-19 15:57:00
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans=0
        A=[list(x) for x in A]
        for x in zip(*A):
            if list(x)!=sorted(x):
                ans+=1
        return ans
