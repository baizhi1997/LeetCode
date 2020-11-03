
# @Title: 不同路径 (Unique Paths)
# @Author: qinxinlei
# @Date: 2018-09-28 09:45:02
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def C(x,y):
            if y==0:
                return 1
            return x*C(x-1,y-1)/y
        x=m+n-2
        y=min(m,n)-1
        return C(x,y)
