
# @Title: 写字符串需要的行数 (Number of Lines To Write String)
# @Author: qinxinlei
# @Date: 2018-10-19 11:11:26
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        i=1
        j=0
        for s in S:
            tmp=widths[ord(s)-97]
            j+=tmp
            if j>100:
                j=tmp
                i+=1
        return [i,j]
