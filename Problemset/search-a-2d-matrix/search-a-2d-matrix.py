
# @Title: 搜索二维矩阵 (Search a 2D Matrix)
# @Author: qinxinlei
# @Date: 2018-09-26 22:10:14
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=(l+r)/2
            num=matrix[mid//n][mid%n]
            if num==target:
                return True
            elif num<target:
                l=mid+1
            else:
                r=mid-1
        return False

