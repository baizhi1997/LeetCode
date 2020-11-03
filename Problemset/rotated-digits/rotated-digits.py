
# @Title: 旋转数字 (Rotated Digits)
# @Author: qinxinlei
# @Date: 2018-10-22 15:51:05
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans=0
        for num in range(N,0,-1):
            s=str(num)
            if '3' in s or '4' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9'in s:
                ans+=1
        return ans
