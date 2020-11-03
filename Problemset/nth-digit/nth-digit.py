
# @Title: 第N个数字 (Nth Digit)
# @Author: qinxinlei
# @Date: 2018-10-03 21:40:49
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        i,p=1,9
        while True:
            n+=p
            p=p*10+9
            i+=1
            if n<p*i:
                return int(str((n+i-1)//i)[(n+i-1)%i])
