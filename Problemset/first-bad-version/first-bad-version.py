
# @Title: 第一个错误的版本 (First Bad Version)
# @Author: qinxinlei
# @Date: 2018-11-05 18:06:50
# @Runtime: 40 ms
# @Memory: N/A

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        while i<n:
            m=(i+n)//2
            if isBadVersion(m):
                n=m
            else:
                i=m+1
        return n
