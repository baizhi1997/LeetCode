
# @Title: 计算各个位数不同的数字个数 (Count Numbers with Unique Digits)
# @Author: qinxinlei
# @Date: 2018-11-24 16:37:40
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[]
        tmp=9
        for i in range(9,0,-1):
            ans.append(tmp)
            tmp*=i
        return sum(ans[:n])+1
