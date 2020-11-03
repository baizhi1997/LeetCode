
# @Title: 重新排序得到 2 的幂 (Reordered Power of 2)
# @Author: qinxinlei
# @Date: 2018-11-24 14:02:49
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        s=sorted(str(N))
        l=len(str(N))
        i=1
        while len(str(i))<l:
            i*=2
        while i<10*N:
            if s==sorted(str(i)):
                return True
            i*=2
        return False
