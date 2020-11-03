
# @Title: 快乐数 (Happy Number)
# @Author: qinxinlei
# @Date: 2018-10-03 17:02:24
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set1=set()
        while n not in set1:
            set1.add(n)
            temp=0
            while n:
                n,val=divmod(n,10)
                temp+=val**2
            n=temp
        return True if n==1 else False
