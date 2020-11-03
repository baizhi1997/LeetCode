
# @Title: 整数反转 (Reverse Integer)
# @Author: qinxinlei
# @Date: 2018-10-02 13:30:56
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit=pow(2,31)
        if x<0:
            x=-int(str(x)[:0:-1])
            if x<-limit:
                return 0
        else:
            x=int(str(x)[::-1])
            if x>=limit:
                return 0
        return x
