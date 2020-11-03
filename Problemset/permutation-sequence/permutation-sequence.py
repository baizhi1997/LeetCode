
# @Title: 排列序列 (Permutation Sequence)
# @Author: qinxinlei
# @Date: 2018-10-16 14:13:27
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans=''
        nums=[i for i in range(1,n+1)]
        tmp=1
        for num in nums:
            tmp*=num
        k-=1
        while n:
            tmp//=n
            ans+=str(nums.pop(k//tmp))
            k%=tmp
            n-=1
        return ans
