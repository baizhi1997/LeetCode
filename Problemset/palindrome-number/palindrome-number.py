
# @Title: 回文数 (Palindrome Number)
# @Author: qinxinlei
# @Date: 2018-10-02 15:01:27
# @Runtime: 152 ms
# @Memory: N/A

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10==0 and x):
            return False
        y=0
        while x>y:
            y*=10
            x,val=divmod(x,10)
            y+=val
        return x==y or x==y//10
