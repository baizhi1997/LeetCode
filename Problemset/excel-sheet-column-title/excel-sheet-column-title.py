
# @Title: Excel表列名称 (Excel Sheet Column Title)
# @Author: qinxinlei
# @Date: 2018-10-09 12:10:24
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans=''
        while n:
            n,val=divmod(n-1,26)
            ans+=(chr(ord('A')+val))
        return ans[::-1]
