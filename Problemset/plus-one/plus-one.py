
# @Title: 加一 (Plus One)
# @Author: qinxinlei
# @Date: 2018-09-26 20:42:38
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l=len(digits)
        flag=True
        for i in range(l)[::-1]:
            if flag:
                digits[i]+=1
            if digits[i]==10:
                digits[i]=0
            else:
                flag=False
                break
        if flag:
            digits.insert(0,1)
        return digits
