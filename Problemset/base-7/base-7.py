
# @Title: 七进制数 (Base 7)
# @Author: qinxinlei
# @Date: 2018-10-09 22:28:24
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        pre='-' if num<0 else ''
        num=abs(num)
        ans=""
        while num:
            num,val=divmod(num,7)
            ans+=str(val)
        return pre+ans[::-1]
