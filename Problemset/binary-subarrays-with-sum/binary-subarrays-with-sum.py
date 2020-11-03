
# @Title: 和相同的二元子数组 (Binary Subarrays With Sum)
# @Author: qinxinlei
# @Date: 2018-12-04 14:25:33
# @Runtime: 76 ms
# @Memory: N/A

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        tmp=[0]*(len(A)+1)
        tmp[0]=1
        cur=0
        ans=0
        for a in A:
            cur+=a
            x=cur-S
            if x>=0:
                ans+=tmp[x]
            tmp[cur]+=1
        return ans
