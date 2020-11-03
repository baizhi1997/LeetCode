
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: qinxinlei
# @Date: 2018-09-30 19:48:32
# @Runtime: 76 ms
# @Memory: N/A

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        pre=0
        for i in s[::-1]:
            n=dic[i]
            if pre<=n:
                ans+=n
            else:
                ans-=n
            pre=n
        return ans
    
