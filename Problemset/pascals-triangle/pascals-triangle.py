
# @Title: 杨辉三角 (Pascal's Triangle)
# @Author: qinxinlei
# @Date: 2018-10-24 20:56:44
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        ans=[[1]]
        for i in range(1,numRows):
            tmp=[1]
            for j in range(1,i):
                tmp.append(ans[-1][j]+ans[-1][j-1])
            tmp.append(1)
            ans.append(tmp)
        return ans
