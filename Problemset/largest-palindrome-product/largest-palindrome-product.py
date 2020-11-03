
# @Title: 最大回文数乘积 (Largest Palindrome Product)
# @Author: qinxinlei
# @Date: 2018-11-05 20:12:09
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 9
        for a in range(2,10**n):
            left=10**n-a
            right=int(str(left)[::-1])
            if a**2-4*right>=0:
                x=a-(a**2-4*right)**0.5
                if x//2==x/2:
                    return (10**n*left+right)%1337
