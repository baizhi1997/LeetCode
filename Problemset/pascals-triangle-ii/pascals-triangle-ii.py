
# @Title: 杨辉三角 II (Pascal's Triangle II)
# @Author: qinxinlei
# @Date: 2018-10-24 20:53:45
# @Runtime: 36 ms
# @Memory: N/A

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[1]
        for i in range(rowIndex):
            ans=[1]+[ans[i]+ans[i+1] for i in range(i)]+[1]
        return ans
        
