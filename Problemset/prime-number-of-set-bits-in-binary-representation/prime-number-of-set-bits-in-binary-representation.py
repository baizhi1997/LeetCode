
# @Title: 二进制表示中质数个计算置位 (Prime Number of Set Bits in Binary Representation)
# @Author: qinxinlei
# @Date: 2018-11-17 13:39:27
# @Runtime: 200 ms
# @Memory: N/A

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        set1=set([2,3,5,7,11,13,17,19])
        ans=0
        for num in range(L,R+1):
            if bin(num).count('1') in set1:
                ans+=1
        return ans
