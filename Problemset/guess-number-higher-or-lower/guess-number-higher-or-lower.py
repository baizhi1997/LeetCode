
# @Title: 猜数字大小 (Guess Number Higher or Lower)
# @Author: qinxinlei
# @Date: 2018-11-01 16:00:47
# @Runtime: 20 ms
# @Memory: N/A

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        while l<=n:
            m=(l+n)//2
            flag=guess(m)
            if flag==0:
                return m
            elif flag==1:
                l=m+1
            else:
                n=m-1
