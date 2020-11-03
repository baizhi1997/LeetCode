
# @Title: Z 字形变换 (ZigZag Conversion)
# @Author: qinxinlei
# @Date: 2018-09-30 13:49:03
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>=len(s):
            return s
        s1=[""]*numRows
        i=0
        t=-1
        for k in s:
            s1[i]+=k
            if i==0 or i==numRows-1:
                t=-t
            i+=t
        return ''.join(s1)
