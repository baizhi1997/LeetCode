
# @Title: Excel表列序号 (Excel Sheet Column Number)
# @Author: qinxinlei
# @Date: 2018-10-03 16:33:40
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for c in s:
            ans=ans*26+ord(c)-ord('A')+1
        return ans
